def is_simple_number(x):
    divider = 2
    while divider < x:
        if x % divider == 0:
            return False
        divider += 1
    return True

import os
import time

symbol_len = 1  # размер буфера чтения
mass_number = []
mass_digit = []
count_1, count_2, count_3 = 0, 0, 0
even_number, odd_number = 0, 0
even_digit, odd_digit = 0, 0
simple_digit, not_simple_digit = 0, 0
try:
    start = time.time()
    i = -1
    with open("text.txt", "r") as file:
        symbol = file.read(symbol_len)
        if not symbol:
            print("\nФайл text.txt пустой.")

        while symbol:
            if symbol == " ":
                mass_number.append(" ")
                i += 1

            while (symbol < '0' or symbol > '9') and symbol:
                symbol = file.read(symbol_len)
            while (symbol >= '0' and symbol <= '9') and symbol:
                mass_number.append(symbol)
                i += 1
                if int(symbol) % 2 == 0:
                    count_1 += 1
                    even_number += 1
                else:
                    count_1 += 1
                    odd_number += 1

                symbol = file.read(symbol_len)
        print(f"Program time:{time.time()-start} seconds.")

    print("Чётных цифр ==>", round((((even_number * 100) / count_1)), 1), "%")
    print("Нечётных цифр ==>", round((((odd_number * 100) / count_1)), 1), "%\n")

    print(mass_number)
    print(i)
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.")
