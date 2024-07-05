"""
Задание
1. Сгенерируйте с использованием функции range (случайный шаг от 3 до 5)
массив, содержащий отсортированные числа от 10 до 250 млн.
Можно использовать функцию randomint из модуля random для ещё большей
рандомизации значений, но для целей работы алгоритма бинарного поиска
проследите, чтобы значения в массиве были отсортированы.
2. Сгенерируйте с помощью list comprehensions и функции randomint
(встроенный модуль random) 10 случайных чисел.
3. Напишите функцию для алгоритма линейного поиска.
4. Напишите функцию для алгоритма бинарного поиска.
5. Проверьте наличие ранее сгенерированных случайных чисел в массиве с
помощью алгоритмов линейного и бинарного поиска, замерьте время
"""

import random
import time


def generate_sorted_array():
    start = 10
    end = 250_000_000
    step_choices = [3, 4, 5]
    array = []
    current = start

    while current <= end:
        array.append(current)
        current += random.choice(step_choices)

    return array


def generate_random_numbers(num=10, lower_bound=10, upper_bound=250_000_000):
    return [random.randint(lower_bound, upper_bound) for _ in range(num)]


def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":

    sorted_array = generate_sorted_array()
    print(f"Generated sorted array of length {len(sorted_array)}")

    random_numbers = generate_random_numbers()
    print("Generated random numbers:", random_numbers)

    linear_search_times = []
    for number in random_numbers:
        start_time = time.time()
        result = linear_search(sorted_array, number)
        end_time = time.time()
        linear_search_times.append(end_time - start_time)
        print(
            f"Linear search for {number}: {'Found' if result != -1 else 'Not found'}, time: {end_time - start_time} seconds")

    binary_search_times = []
    for number in random_numbers:
        start_time = time.time()
        result = binary_search(sorted_array, number)
        end_time = time.time()
        binary_search_times.append(end_time - start_time)
        print(
            f"Binary search for {number}: {'Found' if result != -1 else 'Not found'}, time: {end_time - start_time} seconds")

    print("Linear search times:", linear_search_times)
    print("Average linear search time:", sum(linear_search_times) / len(linear_search_times))

    print("Binary search times:", binary_search_times)
    print("Average binary search time:", sum(binary_search_times) / len(binary_search_times))