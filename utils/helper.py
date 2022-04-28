from datetime import datetime
from models.model import *
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/66.0",
           "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
           "Connection": "close", "Upgrade-Insecure-Requests": "1"}


def scrapeProduct(url, priceDB):
    sku, shortenURL = URL(url).urlShortening()
    status = checkLastScrapeTime(sku, priceDB)
    if status and sku:
        page = requests.get(shortenURL, headers=headers)
        if page.status_code != 200:
            return None, None, status
        soup1 = BeautifulSoup(page.content, "html.parser")
        title = soup1.find(id='productTitle').get_text().strip()
        price = float(soup1.find('span', {'class': 'a-price-whole'}).get_text().strip().split('\n')[0])
        ratingsMap = scrapeReview(soup1)
        obj = Product(product_id=shortenURL, productTitle=title, productPrice=price, ratingsMap=ratingsMap)
        return sku, obj, status
    return None, None, status


def checkLastScrapeTime(sku, priceDB) -> bool:
    if sku in priceDB:
        lastEntry = priceDB[sku][-1]['timestamp']
        duration = datetime.now() - datetime.strptime(lastEntry, "%Y-%m-%d %H:%M:%S")
        if duration.total_seconds() > 3600:
            return True
        else:
            return False
    return True


def scrapeReview(soup):
    table = soup.find(id='histogramTable')
    ratingsMap = {}
    for i in range(5):
        ratingsMap[5 - i] = table.find_all('tr')[i].find_all('td')[2].get_text().strip()
    return ratingsMap
