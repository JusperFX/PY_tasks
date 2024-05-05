"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

Пример
На входе:
s = 12
p = 27
На выходе:
3 9
"""

s = 12
p = 35
list_1 = []

for el in range(1, 1001):
    for elem in range(1, 1001):
        if s == el + elem and p == el * elem:
            list_1.append(((min(el, elem), max(el, elem))))

list_1 = set(list_1)

for item in list_1:
    print(item)