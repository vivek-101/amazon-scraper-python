import re


class URL:
    def __init__(self, url):
        self.url = url

    def urlShortening(self):
        try:
            sku = re.search("dp\/\w{10}\/", self.url).group()
            shortenURL = "https://www.amazon.in/" + sku
            return sku, shortenURL
        except AttributeError as e:
            return None, None


class Product:
    def __init__(self, product_id, productTitle, productPrice, productDescription="", ratingsMap={}):
        self.productId = product_id
        self.productTitle = productTitle
        self.productPrice = productPrice
        self.productDescription = productDescription
        self.ratingsMap = ratingsMap


class Prices:
    def __init__(self, timestamp, price):
        self.timestamp = timestamp
        self.price = price
