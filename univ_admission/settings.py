BOT_NAME = 'univ_admission'

SPIDER_MODULES = ['univ_admission.spiders']
NEWSPIDER_MODULE = 'univ_admission.spiders'

# 遵守網站規範
USER_AGENT = 'Mozilla/5.0 (compatible; univ-admission-bot/1.0; +https://github.com/your-repo)'
DOWNLOAD_DELAY = 2  # 2秒延遲
RANDOMIZE_DOWNLOAD_DELAY = 0.5
ROBOTSTXT_OBEY = True  # 遵守 robots.txt

# 輸出設定
FEEDS = {
    'admissions.json': {'format': 'json'},
    'admissions.csv': {'format': 'csv'},
}

# Pipeline 啟用
ITEM_PIPELINES = {
    'univ_admission.pipelines.SQLitePipeline': 300,
}
