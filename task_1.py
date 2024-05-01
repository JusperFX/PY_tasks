"""
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while.
Input: 5
Output: 120 
"""

num = 5
f = 1

# while num > 1:
#     f *= num #умножение и присваивание
#     num -= 1
# print(f)

# for elem in range(1, num + 1):
#     f *= elem
# print(f)

def factorial(num, f=1):
    if num == 0:
        return f
    return factorial(num - 1, f*num)

print(factorial(num))