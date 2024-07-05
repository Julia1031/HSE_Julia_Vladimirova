"""
Задание 1 (парсинг)
Напишите скрипт, который будет производить сбор данных с выбранной вами
страницы на сайте ЦБ РФ либо осуществлять загрузку xsl, xslx, pdf, csv или иного
файла с данными в рабочую директорию с последующим его парсингом.
У класса должен быть только один публичный метод start(). Все остальные методы,
содержащие логику по выгрузке и сохранению данных, должны быть приватными.
Определите структуру для хранения. Для ключевой ставки ЦБ РФ это может быть
словарь (dict), где ключом будет выступать дата, а значением — размер ключевой
ставки на указанную дату.
Оберните весь написанный код парсера в класс ParserCBRF.
"""


import requests
from bs4 import BeautifulSoup
import csv
import os
import json


class ParserCBRF:
    def __init__(self):
        self.url = 'https://www.cbr.ru/hd_base/KeyRate/'
        self.data = {}

    def start(self):
        self._fetch_data()
        self._parse_data()
        self._save_data()

    def _fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.html = response.text
        else:
            raise Exception("Failed to fetch data from CBR website")

    def _parse_data(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        table = soup.find('table', {'class': 'data'})

        if not table:
            raise Exception("Failed to find data table on the page")

        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) >= 2:
                date = columns[0].text.strip()
                rate = columns[1].text.strip().replace(',', '.')
                try:
                    rate = float(rate)
                    self.data[date] = rate
                except ValueError:
                    continue

    def _save_data(self):
        filename = 'key_rate_data.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Key Rate'])
            for date, rate in self.data.items():
                writer.writerow([date, rate])
        print(f"Data has been saved to {filename}")

    def serialize(self, filepath='data.json'):
        with open(filepath, 'w') as file:
            json.dump(self.data, file, indent=4)
        print(f"Data has been serialized to {filepath}")

    def deserialize(self, filepath='data.json'):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                self.data = json.load(file)
            print(f"Data has been deserialized from {filepath}")
        else:
            print(f"File {filepath} does not exist")


if __name__ == "__main__":
    parser = ParserCBRF()
    parser.start()
    parser.serialize()
    parser.deserialize()