import re 
import time 
import json
import random
import string

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from pandas.io.json import json_normalize

class BrowserDriverCrawler:
    def __init__(self, dataPath):
        self.dataPath = dataPath
    
    def readData(self):
        df = pd.read_csv(self.dataPath, usecols=['公司'])
        df.rename(columns={"公司": "company"}, inplace=True)

        # clean data 
        ll = df['company'][(~df['company'].str.contains("查不到", regex=False)) &
                           (~df['company'].str.contains("?", regex=False)) &
                           (~df['company'].str.contains("[a-zA-Z0-9]"))
                                      ].tolist()
        return ll

    def FirefoxCrawler(self, searchName):
        # Open Firefox
        driver = webdriver.Firefox()
        url = "https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do"
        driver.get(url)
        
        time.sleep(random.randint(2, 3))
        
        # Send Keywords
        driver.find_element_by_id('qryCond').send_keys(searchName)
        driver.find_element_by_id("qryBtn").click()

        time.sleep(random.randint(2, 3))
        
        # ButtonClick
        href = driver.find_element_by_class_name("hover").get_attribute('href')
        src = driver.execute_script("window.open('" + href +"');")

        time.sleep(random.randint(2, 3))

        # Switch tab
        handles = driver.window_handles
        driver.switch_to.window(handles[1])

        # HTML Parser 
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        driver.quit()
        return soup
    
    def ExtractDataToJson(self, searchName):
        soup = self.FirefoxCrawler(searchName)
        txt = soup.findAll("table", class_="table table-striped")[13].text
        pre = re.findall("[^\n\t\xa0]+", txt)


        d = {"公司基本資料": {
            "統一編號": "",
            "公司狀況": "",
            "公司名稱": "",
            "章程所訂外文公司名稱": "",
            "資本總額(元)": "",
            "實收資本額(元)": "",
            "代表人姓名": "",
            "公司所在地": "",
            "登記機關": "",
            "核准設立日期": "",
            "最後核准變更日期": "",
            "複數表決權特別股": "",
            "對於特定事項具否決權特別股": "",
            "特別股股東被選為董事、監察人之禁止或限制或當選一定名額之權利": "",
            "所營事業資料": ""
            }
            }

        ix = 0
        while ix < len(pre):
            if (pre[ix] == "統一編號") and (pre[ix + 1] != "公司狀況"):
                d['公司基本資料']['統一編號'] = pre[ix + 1]
    
            elif (pre[ix] == "公司狀況") and (pre[ix + 1] != "公司名稱"):
                d['公司基本資料']['公司狀況'] = pre[ix + 1]

            elif (pre[ix] == "公司名稱") and (pre[ix + 1] != "章程所訂外文公司名稱"):
                d['公司基本資料']['公司名稱'] = pre[ix + 1]

            elif (pre[ix] == "章程所訂外文公司名稱") and (pre[ix + 1][:4] != "資本總額"):
                d['公司基本資料']["章程所訂外文公司名稱"] = pre[ix + 1]

            elif pre[ix][:4] == "資本總額":
                num = re.findall("[0-9]+", pre[ix].replace(",", ""))
                d['公司基本資料']["資本總額(元)"] = int(str(num).strip("['").strip("']"))

            elif (pre[ix] == "實收資本額(元)") and (pre[ix + 1] != "代表人姓名"):
                d['公司基本資料']["實收資本額(元)"] = int(pre[ix + 1].replace(",", ""))

            elif (pre[ix] == "代表人姓名") and (pre[ix + 1] != "公司所在地"):
                d['公司基本資料']["代表人姓名"] = pre[ix + 1]

            elif (pre[ix] == "公司所在地") and (pre[ix + 1] != "電子地圖"):
                d['公司基本資料']["公司所在地"] = pre[ix + 1]

            elif (pre[ix][:4] == "登記機關"):
                d['公司基本資料']["登記機關"] = pre[ix][4:]

            elif (pre[ix][:6] == "核准設立日期"):
                d['公司基本資料']["核准設立日期"] = pre[ix][6:]

            elif (pre[ix][:8] == "最後核准變更日期"):
                d['公司基本資料']["最後核准變更日期"] = pre[ix][8:]

            elif (pre[ix][:8] == "複數表決權特別股"):
                d['公司基本資料']["複數表決權特別股"] = pre[ix][8:]

            elif (pre[ix][:13] == "對於特定事項具否決權特別股"):
                d['公司基本資料']["對於特定事項具否決權特別股"] = pre[ix][13:]

            elif (pre[ix] == "特別股股東被選為董事、監察人之禁止或限制或當選一定名額之權利") and (pre[ix + 1] != "所營事業資料"):
                d['公司基本資料']["特別股股東被選為董事、監察人之禁止或限制或當選一定名額之權利"] = pre[ix + 1]

            elif (pre[ix][:6] == "所營事業資料"):
                tmp = []
                ii = ix + 1
                while ii < 60:
                    try: 
                        tt = pre[ii]
                        tmp.append(tt)
                    except:
                        pass
                    finally:
                        ii += 1
                d['公司基本資料']["所營事業資料"] = tmp
            ix += 1
        return d

def main():
    dataPath = "./data/exampleData.csv" 
    f = BrowserDriverCrawler(dataPath) 
    search_list = f.readData() 

    result = []
    for searchName in search_list: 
        print("Current Running: {}".format(searchName))
        info = f.ExtractDataToJson(searchName)
        result.append(info)

    with open('./results/company.json', 'w') as outfile:  
        json.dump(result, outfile, ensure_ascii=False)

if __name__ == "__main__":
    main()