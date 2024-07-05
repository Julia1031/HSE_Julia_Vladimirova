"""
Задание
Опишите любую абстракцию (желательно юридическую, но вы можете выбрать любую
другую) с помощью инструментов ООП (например, Истец-Ответчик, ПравоОбязательство, Срок, Судья и др.).
Придумайте атрибуты и методы для абстракции. Если ничего не приходит на ум, просто
дополните абстракцию (класс) из домашнего задания № 7 любыми атрибутами и
методами на ваше усмотрение.
Пример с автомобилем:
class Car:
def __init__(self, brand, model, year):
self.brand = brand
self.model = model
self.year = year
self.is_engine_working = False
def start_engine(self):
self.is_engine_working = True
print("Двигатель включён")
def stop_engine(self):
self.is_engine_working = False
print("Двигатель выключён")
def go_to(self, destination):
print(f"{self.brand} {self.model} {self.year} года выпуска"
f"направляется в сторону {destination}")
"""


class Participant:
    def __init__(self, name, inn, role):

        self.name = name
        self.inn = inn
        self.role = role

    def __str__(self):
        return f"{self.role}: {self.name}, ИНН: {self.inn}"


class CourtCase:
    def __init__(self, case_number):

        self.case_number = case_number
        self.plaintiff = None
        self.defendant = None
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ""

    def set_plaintiff(self, name, inn):

        self.plaintiff = Participant(name, inn, "Истец")

    def set_defendant(self, name, inn):

        self.defendant = Participant(name, inn, "Ответчик")

    def set_a_listening_datetime(self, listening_datetime):

        self.listening_datetimes.append(listening_datetime)

    def make_a_decision(self, verdict):

        self.verdict = verdict
        self.is_finished = True

    def __str__(self):

        return (f"Номер дела: {self.case_number}\n"
                f"{self.plaintiff}\n"
                f"{self.defendant}\n"
                f"Даты заседаний: {self.listening_datetimes}\n"
                f"Завершено: {self.is_finished}\n"
                f"Решение: {self.verdict}")


if __name__ == "__main__":
    case_number = input("Введите номер дела: ")
    court_case = CourtCase(case_number)

    plaintiff_name = input("Введите имя истца: ")
    plaintiff_inn = input("Введите ИНН истца: ")
    court_case.set_plaintiff(plaintiff_name, plaintiff_inn)

    defendant_name = input("Введите имя ответчика: ")
    defendant_inn = input("Введите ИНН ответчика: ")
    court_case.set_defendant(defendant_name, defendant_inn)

    while True:
        action = input("Хотите добавить дату заседания? (да/нет): ").strip().lower()
        if action == 'да':
            listening_datetime = input("Введите дату и время заседания (в формате YYYY-MM-DDTHH:MM:SS): ")
            court_case.set_a_listening_datetime(listening_datetime)
        else:
            break

    verdict = input("Введите решение по делу: ")
    court_case.make_a_decision(verdict)

    print(court_case)