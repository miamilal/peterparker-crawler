# peterparker-crawler
公司/工廠登記資料爬蟲程式 (Web crawler by using python selenium)。

## 使用方法

```shell
$ git clone https://github.com/siansiansu/peterparker-crawler.git
$ pip install -p Pipfile.lock  # install requirements
$ pip shell
$ python3 crawler.py
```

## 測試的公司名稱
- 華創實業股份有限公司
- 崇友實業股份有限公司
- 日月光半導體製造股份有限公司
- 鴻海有限公司

> 注意每間公司的表格資料可能會些許不同，抓取資料下來後得另外清洗資料。

## 網站首頁 
[商工登記公示資料查詢服務首頁](https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do#)，輸入關鍵字查詢登記的公司。

![](https://i.imgur.com/lvLE6aR.png)

## 公司詳細資訊
點進去公司詳細資訊後，可以看到「公司基本資料」、「董監事資料」、「經理人資料」、「分公司資料」、「跨域資料」，Scripts 只有抓取公司基本資料，其餘的部分可以依照同樣的方式使用 selenium 抓取。 

![](https://i.imgur.com/bqxivg8.png)

## 資料結構
以 JSON 檔的方式儲存在 `./results` 資料夾裡面。

![](https://i.imgur.com/nLQFxID.png)

