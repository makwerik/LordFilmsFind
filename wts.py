import requests
import random

from bs4 import BeautifulSoup


class WhatToSee:
    def __init__(self, url):
        self.url = url
        self.movies_on_the_page = 30
        self.all_films = random.randint(0, 15210)

    def __find_page_and_films(self):
        page_number = -(-self.all_films // self.movies_on_the_page)

        film_on_page = self.all_films % self.movies_on_the_page
        if film_on_page == 0:
            film_on_page = self.movies_on_the_page

        return page_number, film_on_page

    def get_film(self):
        p, f = self.__find_page_and_films()
        response = requests.get(f'{self.url}{p}/')
        soup = BeautifulSoup(response.content, 'lxml')

        film = soup.findAll(class_='th-item')[f-1]

        ref_film = {
            "Name": film.find(class_="th-title").text,
            "KP": film.find(class_="th-rate th-rate-kp").text,
            "IMDB": film.find(class_="th-rate th-rate-imdb").text,
            "Series": film.find(class_="th-series").text,
            "Link": film.find("a").get("href")
        }
        return ref_film


if __name__ == '__main__':
    wts = WhatToSee('https://m.mmcfilm.ru/filmy/page/')
    print(wts.get_film())