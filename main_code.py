import math

with open('text.txt','r') as file:
    sequence = file.read()
count, even_num, odd_num  = 0, 0, 0
main_mass = list(map(int, sequence.split(" ")))

# ПОИСК ВСЕХ ЧЁТНЫХ И НЕЧЁТНЫХ ЦИФР В ПОСЛЕДОВАТЕЛЬНОСТИ
for i in range(len(sequence)):
    if sequence[i] == " ":
        continue
    if (int(sequence[i])) % 2 == 0:
        even_num += 1
        count += 1
    else:
        odd_num += 1
        count += 1
print("Чётных цифр ==>", round((((even_num * 100) / count)), 1), "%")
print("Нечётных цифр ==>", round((((odd_num * 100) / count)), 1), "%\n")
count, even_num, odd_num  = 0, 0, 0

# ПОИСК ВСЕХ ЧЁТНЫХ И НЕЧЁТНЫХ ЧИСЕЛ В ПОСЛЕДОВАТЕЛЬНОСТИ
for i in range(len(sequence)):
    if sequence[i] == " ":
        if int(sequence[i - 1]) % 2 == 0:
            count += 1
            even_num += 1
        else:
            count += 1
            odd_num += 1
if (int(sequence[-1])) % 2 == 0:
    count += 1
    even_num += 1
else:
    count += 1
    odd_num += 1
print("Чётных чисел ==>", round((((even_num * 100) / count)), 1), "%")
print("Нечётных чисел ==>", round((((odd_num * 100) / count)), 1), "%\n")
count = 0

# АЛГОРИТМ ПОИСКА ВСЕХ ПРОСТЫХ ЧИСЕЛ В ПОСЛЕДОВАТЕЛЬНОСТИ
simple_num, not_simple_num = 0, 0
for i in range(0, len(main_mass)):
    k = 0
    for j in range(2, (int(main_mass[i]) // 2) + 1):
        if (int(main_mass[i])) % j == 0:
            k += 1
    if k <= 0:
        count += 1
        simple_num += 1
    else:
        count += 1
        not_simple_num += 1
print("Простых чисел ==>", round(((simple_num * 100) / count), 1), "%")
print("Непростых чисел ==>", round(((not_simple_num * 100) / count), 1), "%")
