import scrapy
from univ_admission.items import JbcrcItem
from urllib.parse import urljoin

class JbcrcSpider(scrapy.Spider):
    name = 'jbcrc'
    allowed_domains = ['jbcrc.edu.tw']
    start_urls = [
        'https://www.jbcrc.edu.tw/',
        'https://www.jbcrc.edu.tw/latest-news/',
        'https://www.jbcrc.edu.tw/latest-news/admission-information/',
        'https://www.jbcrc.edu.tw/latest-news/department-information/'
    ]  # 多頁入口

    def parse(self, response):
        item = JbcrcItem()
        item['source'] = '大學招生委員會聯合會'

        # 抓「最新消息」列表（依網站結構調整）
        news_items = response.css('div.news-list a, .latest-news a, .news a, li a::attr(href), a[href*="latest-news"]')
        
        for a in news_items:
            item['title'] = a.css('::text').get(default='').strip()
            href = a.attrib.get('href', '')
            item['url'] = urljoin(response.url, href)
            
            # 日期從父元素或時間標籤抓取
            date_elem = a.xpath('./parent::li//text() | ./parent::*//span[contains(@class,"date")]//text() | ./following-sibling::*/text()')
            item['date'] = date_elem.get(default='').strip()
            
            item['category'] = response.url.split('/')[-1] or '最新消息'
            
            # 自動偵測學年度
            if any(year in item['title'].lower() for year in ['115', '114', '113']):
                item['year'] = next(year for year in ['115', '114', '113'] if year in item['title'].lower())
            else:
                item['year'] = '未知'
            
            if item['title']:  # 只 yield 有標題的
                yield item

        # 發現更多連結繼續爬（動態擴展）
        next_pages = response.css('a:contains("下一頁"), a.next::attr(href)')
        for next_page in next_pages:
            yield response.follow(next_page, self.parse)
