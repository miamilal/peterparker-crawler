# peterparker-crawler
公司/工廠登記資料爬蟲程式 (Web crawler by using python selenium)，原始專案不公開，所以只放測試資料集。

## 使用方法

```shell
$ git clone https://github.com/siansiansu/peterparker-crawler.git
$ pip install -p Pipfile.lock  # install requirements
$ pip shell
$ python3 crawler.py

# Current Running: 華創實業股份有限公司
# Current Running: 崇友實業股份有限公司
# Current Running: 日月光半導體製造股份有限公司
# Current Running: 鴻海有限公司
# Current Running: 采鈺科技股份有限公司
```

## 測試的公司名稱
- 華創實業股份有限公司
- 崇友實業股份有限公司
- 日月光半導體製造股份有限公司
- 鴻海有限公司
- 采鈺科技股份有限公司

> 每間公司的資料會些許不同，視情況加入 TryExcept 例外處理。

## 網站首頁 
點進去[商工登記公示資料查詢服務首頁](https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do#)，輸入關鍵字查詢登記的公司。

![](https://i.imgur.com/lvLE6aR.png)

## 公司詳細資訊
按一下公司的詳細資訊按鈕，可以看到「公司基本資料」、「董監事資料」、「經理人資料」、「分公司資料」、「跨域資料」，我只有抓取公司的基本資料，其餘部分可以依照類似的方式抓取資料。 

![](https://i.imgur.com/bqxivg8.png)

## 資料結構
以 JSON 檔的格式儲存在 `./results` 資料夾裡面。

![](https://i.imgur.com/nLQFxID.png)

## Contact Me
Alex Su: minsiansu@gmail.com