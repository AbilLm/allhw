import requests
from parsel import Selector
from pprint import pprint

class House:
    MAIN_URL = 'https://www.house.kg/snyat'
    BASE_URL = 'https://www.house.kg/'


    def get_html(self, url=MAIN_URL):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text

    def paginate(self, from_page=1, to_page=5):
        for page in range(from_page, to_page + 1):
            yield f"{self.MAIN_URL}/?page={page}"

    def get_house(self, html):
        selector = Selector(text=html)
        houses = selector.css('.main-wrapper')
        all_houses = []
        for house in houses:
            title = house.css(".title a::text").getall()[0].strip()
            link = house.css(".title a").attrib.get("href")
            full_link = f"{self.BASE_URL}{link}"
            all_houses.append({
                "title": title,
                "link": full_link
            })
        return all_houses


    def get_house_links(self):
        links =[]
        for url in self.paginate(1,3):
            html = self.get_html(url)
            house_data = self.get_house(html)
            links.extend(house_data)
        return links

if __name__ == "__main__":
    scraper = House()
    house_links = scraper.get_house_links()
    pprint(house_links)
    print(len(house_links))