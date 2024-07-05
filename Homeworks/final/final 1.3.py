"""
Задание № 1: циклы и функции
Задача 3
Монотонная последовательность — это последовательность, элементы которой с
увеличением номера только возрастают, или, наоборот, только убывают.
Массив nums является монотонно возрастающим, если верно i <= j, nums[i] <= nums[j].
Напишите функцию, которая будет принимать в себя массив, состоящий из цифр, и
возвращать:
 true — если массив является монотонным,
 false — в обратном случае.
"""

def is_monotonic(nums):

    if all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)):
        return True
    if all(nums[i] >= nums[i+1] for i in range(len(nums) - 1)):
        return True
    return False

if __name__ == "__main__":
    user_input = input("Введите последовательность чисел, разделенных пробелом: ")
    nums = list(map(int, user_input.split()))
    result = is_monotonic(nums)
    print(f"Последовательность {nums} является монотонной: {result}")