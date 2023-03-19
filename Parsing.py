import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://omsk-nedvizhimost.ru/kvartiry/prodam/1-komnatnye/"

names = []
adress = []
cost = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36"
}

def connect():
    padge = requests.get(url, headers=headers)
    print(padge)

def parse():
    padge = requests.get(url, headers=headers)

    soup = BeautifulSoup(padge.text, "html.parser")
    # soup = BeautifulSoup(padge.text, "lxml")

    blockName = soup.findAll('h3')
    blockAdress = soup.findAll('div', class_='areas')
    blockCost = soup.findAll('div', class_='a_blok_txt_r')
    #blockCost = soup.find_all('span', class_='znakrub')

    for res in blockName:
        names.append(res.text.strip().replace('\xa0', ' '))
    for res in blockAdress:
        adress.append(res.text.strip().replace('\xa0', ' '))
    for res in blockCost:
        text = res.text.strip()
        text = text[:-(len(res.find('span', class_='price2').text.strip())+4)] # Убираем лишнюю информацию и оставляем голую цену
        print(text)
        cost.append(text)

    df = pd.DataFrame({'Название': names,
                       'Адрес': adress,
                       'Цена': cost})

    df.to_excel('Realty.xlsx', index=False)

