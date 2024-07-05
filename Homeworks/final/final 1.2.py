"""
Задание № 1: циклы и функции
Задача 2
Напишите функцию-конвертер из системы римских цифр в знакомую нам десятичную
целочисленную.
"""


def roman_to_int(s):

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

if __name__ == "__main__":
    roman_input = input("Введите римское число: ")
    decimal_output = roman_to_int(roman_input)
    print(f"Десятичное значение римского числа {roman_input} равно {decimal_output}")