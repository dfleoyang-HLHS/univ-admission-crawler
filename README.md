# univ-admission-crawler
20260304
# 台灣大學入學招生爬蟲

爬取「大學招生委員會聯合會」最新消息與115學年度招生公告，存入 SQLite 資料庫。

## 快速開始

**Codespaces（推薦）**
1. 點擊 "Code" → "Codespaces" → "Create codespace"
2. Terminal: `pip install -r requirements.txt && scrapy crawl jbcrc`

**本地執行**
```bash
pip install -r requirements.txt
scrapy crawl jbcrc -o admissions.json
