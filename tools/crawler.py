import time 
import random

from bs4 import BeautifulSoup
from selenium import webdriver

class BrowserDriverCrawler(object):
    def __init__(self):
        self.url = "https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do" 
    
    def LaunchFirefox(self, searchName):
        # Open Firefox
        driver = webdriver.Firefox()
        driver.get(self.url)
        
        time.sleep(random.randint(1, 3))
        
        # Send Keywords
        driver.find_element_by_id('qryCond').send_keys(searchName)
        driver.find_element_by_id("qryBtn").click()

        time.sleep(random.randint(1, 3))
        
        # Click Button
        href = driver.find_element_by_class_name("hover").get_attribute('href')
        src = driver.execute_script("window.open('" + href +"');")

        time.sleep(random.randint(1, 3))

        # Switch Tab
        handles = driver.window_handles
        driver.switch_to.window(handles[1])

        # HTML Parser 
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        driver.quit()
        return soup
