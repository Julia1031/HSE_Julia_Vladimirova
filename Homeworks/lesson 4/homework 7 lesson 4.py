"""
Задание
Реализуйте класс CourtCase.
При вызове метода конструктора экземпляра (__init__) должны создаваться
следующие атрибуты экземпляра:
● case_number (строка с номером дела — обязательный параметр) передаётся в
качестве аргумента при создании экземпляра
● case_participants (список по умолчанию пустой)
● listening_datetimes (список по умолчанию пустой)
● is_finished (значение по умолчанию False)
● verdict (строка по умолчанию пустая)
У экземпляра должны быть следующие методы:
● set_a_listening_datetime — добавляет в список listening_datetimes судебное
заседание (структуру можете придумать сами)
● add_participant — добавляет участника в список case_participants (можно просто
ИНН)
● remove_participant — убирает участника из списка case_participants
● make_a_decision — вынести решение по делу, добавить verdict и сменить
атрибут is_finished на True
"""

class CourtCase:
    def __init__(self, case_number):

        self.case_number = case_number
        self.case_participants = []
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ""

    def set_a_listening_datetime(self, listening_datetime):

        self.listening_datetimes.append(listening_datetime)

    def add_participant(self, participant):

        self.case_participants.append(participant)

    def remove_participant(self, participant):

        if participant in self.case_participants:
            self.case_participants.remove(participant)

    def make_a_decision(self, verdict):
        
        self.verdict = verdict
        self.is_finished = True


def main():
    case_number = input("Введите номер дела: ")
    court_case = CourtCase(case_number)

    while True:
        action = input(
            "Выберите действие: \n1 - Добавить дату заседания\n2 - Добавить участника\n3 - Удалить участника\n4 - Вынести решение\n5 - Завершить\n")

        if action == "1":
            listening_datetime = input("Введите дату и время заседания (в формате YYYY-MM-DDTHH:MM:SS): ")
            court_case.set_a_listening_datetime(listening_datetime)
        elif action == "2":
            participant = input("Введите ИНН участника: ")
            court_case.add_participant(participant)
        elif action == "3":
            participant = input("Введите ИНН участника для удаления: ")
            court_case.remove_participant(participant)
        elif action == "4":
            verdict = input("Введите решение по делу: ")
            court_case.make_a_decision(verdict)
        elif action == "5":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

    print(f"Номер дела: {court_case.case_number}")
    print(f"Участники дела: {court_case.case_participants}")
    print(f"Даты заседаний: {court_case.listening_datetimes}")
    print(f"Завершено: {court_case.is_finished}")
    print(f"Решение: {court_case.verdict}")


if __name__ == "__main__":
    main()