from parsel import Selector
import requests


class CarsKg:
    main_url = "https://cars.kg/offers"
    base_url = "https://cars.kg"

    def get_html(self):
        response = requests.get(self.main_url)
        # print(response.status_code)
        if response.status_code == 200:
            return response.text

    def get_title(self, html):
        selector = Selector(text=html)
        title = selector.css('title::text').get()
        return title
    def get_cars(self, html):
        selector = Selector(text=html)
        cars = selector.css('.catalog-list-item')
        all_cars = []
        for car in cars:
            title = car.css('.catalog-item-caption::text').get().strip()
            mileage = car.css(".catalog-item-mileage::text").get()
            if mileage is not None:
                mileage = mileage.strip()
                thumbnail_url = car.css('.catalog-item-cover img').attrib.get('src')
                price_usd = car.css('.catalog-item-price::text').get()
                price_kgs = car.css('.catalog-item-price::text').get()
                link = car.attrib.get("href")
                all_cars.append({
                "title": title,
                'mileage': mileage,
                'thumbnail_url': thumbnail_url,
                'price_usd': price_usd,
                "price_kgs": price_kgs,
                'link': f"{self.base_url}{link}"
            })
            return all_cars






if __name__ == "__main__":
    scraper = CarsKg()
    html = scraper.get_html()
    #title = scraper.get_title(html)
    #print(title)
    cars = scraper.get_cars(html)
    print(cars)