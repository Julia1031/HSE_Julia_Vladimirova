"""
Реализуйте структуру данных «Участники спора». Она должна представлять собой
список (list) словарей (dict).
Каждый словарь хранит информацию об отдельном участнике. Словарь содержит
пары «ключ-значение» параметрами, то есть характеристиками участника:
наименование, статус, ИНН.
Заполнение данных должно быть произведено пользователем через консоль для трёх
различных участников.
Пример готовой структуры:
[
{“name”: 'ООО "Рога и Копыта"', “status”: "Истец", “inn”: "4545454545"},
{“name”: 'Баширов А.А.', “status”: "Ответчик", “inn”: "32323232323232"},
{“name”: 'Петров А.А.', “status”: "Третье лицо", “inn”: "12121212121212"}
]
Выведите полученные данные в консоль.
"""

participants = []

for i in range(3):
    participant = {}
    print(f"Внесите данные участника  {i + 1}:")
    participant["наименование"] = input("Введите наименование: ")
    participant["статус"] = input("Введите статус (истец / ответчик / третье лицо): ")
    participant["ИНН"] = input("Введите ИНН (10 цифр): ")

    participants.append(participant)

print("Список участников:")
for idx, participant in enumerate(participants, 1):
    print(f"Участник {idx}: {participant}")