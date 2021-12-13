import random
import time

import requests
from bs4 import BeautifulSoup
import fake_useragent
import json

user = fake_useragent.UserAgent().random
header = {'user-agent':user}
prodeject_list = []
iterac_do_conca = 96
numbers = 1

for qqq in range(96):
    numberss = str(numbers)
    url = (f'https://animego.org/anime?sort=a.createdAt&direction=desc&type=animes&page={numberss}')
    numbers += 1
    iterac_do_conca -= 1
    print(iterac_do_conca)
    res = requests.get(url,headers=header)
    soup = BeautifulSoup(res.text,'lxml')
    catalog = soup.find('div',class_='animes-list position-relative')
    anime = catalog.find_all('div',class_='col-12')
    for numm, aniime in enumerate(anime):
        sulka_anime = aniime.find('a').get('href')
        res = requests.get(sulka_anime, headers=header)
        soup = BeautifulSoup(res.text, 'lxml')
        try:
            name = soup.find('div',class_='anime-title').find('h1').text
        except Exception:
            name = 'Незивестно'
        try:
            grade = soup.find('div',class_='pr-2').text.split()
        except Exception:
            grade = 'Незивестно'
        try:
            tip_anime = soup.find('dd', class_='col-6 col-sm-8 mb-1').text
        except Exception:
            tip_anime = 'Незивестно'
        try:
            epizod = soup.find('div',class_='col-3 col-sm-2 col-md text-truncate').text
        except Exception:
            epizod = 'Неизвестно'
        prodeject_list.append(
            {
                'Название аниме': name,
                'Оценка': grade,
                'Тип': tip_anime,
                'Количество эпизодов': epizod,
                'Ссылка на аниме':sulka_anime,
            }
        )

        with open('project.json', 'a', encoding="utf-8") as file:
            json.dump(prodeject_list, file, indent=4, ensure_ascii=False)
    time.sleep(random.randrange(2, 3))