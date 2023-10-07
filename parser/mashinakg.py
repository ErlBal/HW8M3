import requests
from parsel import Selector
from db.shopdb import save_cars, init_db


url = 'https://www.mashina.kg/new/search/'

def get_html():
    response = requests.get(url)
    return response.text

def parse_html(html):
    selector = Selector(text=html)
    return selector


def dbcars():
    html = get_html()
    selector = parse_html(html)
    cars = selector.css('.listing-item.main')
    c = 0
    for car in cars:
        title = car.css('a span[title]::text').get()
        desc = car.css('a span[href]::text').get()
        link = "https://www.mashina.kg"+car.css("a::attr(href)").get()
        price_rough_cut = car.css('.font-big.custom-margins::text').get()
        price_rough_cut2 = car.css('.sign.b-l span.custom-margins.font-small::text').get()
        price = price_rough_cut if price_rough_cut != None else price_rough_cut2

        save_cars(title, desc, link, price)
