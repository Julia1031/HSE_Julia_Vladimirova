"""
Задание
1. Найдите информацию об организациях.
a. Получите список ИНН из файла traders.txt.
b. Найдите информацию об организациях с этими ИНН в файле
traders.json.
c. Сохраните информацию об ИНН, ОГРН и адресе организаций из файла
traders.txt в файл traders.csv.
2. Напишите регулярное выражение для поиска email-адресов в тексте.
Для этого напишите функцию, которая принимает в качестве аргумента текст в виде
строки и возвращает список найденных email-адресов или пустой список, если
email-адреса не найдены.
Используйте датасет на 1 000 сообщений из Единого федерального реестра сведений
о банкротстве (ЕФРСБ) для практики.
Есть датасеты и побольше:
● датасет на 10 000 сообщений,
● датасет на 100 000 сообщений.
Если компьютер слабый, ограничьтесь самым маленьким.
Текст сообщений можно найти по ключу msg_text.
Найдите все email-адреса в датасете и соберите их в словарь, где ключом будет
выступать ИНН опубликовавшего сообщение publisher_inn, а в значении будет
храниться множество set() с email-адресами. Пример:
{
“77010127248512”: {“name_surname@yandex.ru”, “name_surname@mail.ru”}
“77011235421242”: {“name_surname@yandex.ru”, “name_surname@gmail.com”}
…
}
Сохраните собранные данные в файл emails.json.
"""

import json
import csv


inn_list = []
with open('traders.txt', 'r') as f:
    for line in f:
        inn_list.append(line.strip())


inn_info = {}
with open('traders.json', 'r') as f:
    traders_data = json.load(f)
    for trader in traders_data:
        if trader['inn'] in inn_list:
            inn_info[trader['inn']] = {'ogrn': trader['ogrn'], 'address': trader['address']}


with open('traders.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['inn', 'ogrn', 'address'])
    for inn, info in inn_info.items():
        csv_writer.writerow([inn, info['ogrn'], info['address']])

print("Информация сохранена в файл traders.csv.")


import json
import re

def extract_emails_from_text(text):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

def find_emails_in_messages(messages):
    emails_dict = {}

    for message in messages:
        inn = message.get('publisher_inn')
        msg_text = message.get('msg_text')

        if inn not in emails_dict:
            emails_dict[inn] = set()

        emails = extract_emails_from_text(msg_text)
        if emails:
            emails_dict[inn].update(set(emails))

    return emails_dict


with open('1000_efrsb_messages.json', 'r') as file:
    messages = json.load(file)

emails_dict = find_emails_in_messages(messages)

emails_dict = {k: list(v) for k, v in emails_dict.items()}

with open('emails.json', 'w') as output_file:
    json.dump(emails_dict, output_file, indent=4)

print("Email-сохранены в файл emails.json")