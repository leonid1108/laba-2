""" Программа, которая посимвольно читает последовательность чисел из "бесконечного" входного потока данных и
выводит на экран его характеристики в процентном соотношении:
чётных и нечётных цифр, чётных и нечётных чисел и простых чисел. """

import time
import cProfile
import os
import psutil

def is_simple_number(x):
    divider = 2
    if x == 0:
        return False
    while divider < (x**0.5):
        if x % divider == 0:
            return False
        divider += 1
    return True

# Основная функция
def task():
    symbol_len = 1  # Размер буфера чтения
    mass_number = [] # Массив всех цифр и пробелов
    digit = 0 # Все числа в формате int
    counter_len_number = 0 # Счётчик длины числа
    offset_counter = 0 # Счётчик смещения
    flag = True
    index = -1  # Индекс каждого символа, начинаем с -1, т.к индексация в Python начинается с 0
    even_number, odd_number = 0, 0
    even_digit, odd_digit = 0, 0,
    simple_digit, not_simple_digit = 0, 0
    try:
        start = time.time()
        with open("text.txt", "r+") as file:  # Открытие файла
            file.write(" ")
            symbol = file.read(symbol_len) # Читаем первый символ
            if not symbol:            # Обработка исключения пустого файла
                print("\nФайл text.txt пустой.")

            while symbol: # Пока файл не пустой
                while (symbol < '0' or symbol > '9' or symbol == " ") and symbol: # Ищем цифры или пробелы
                    symbol = file.read(symbol_len) # Читаем символ
                while (symbol >= '0' and symbol <= '9' or symbol == " ") and symbol:  # Обрабатываем цифры
                    while symbol != " ": # Считает кол-во цифр в числе, для каждого нового обновляет счётчик
                        counter_len_number += 1
                        break
                    if symbol == " ": # Работа с числами
                        n = counter_len_number
                        while flag:
                            digit += int(mass_number[index-offset_counter])*(10**(counter_len_number-n)) # Алгоритм, который каждый раз суммирует число разряда в переменную digit
                            offset_counter += 1                                      # На выходе получаем число в переменной digit, с которым можно спокойно работать и проверять на простоту
                            n -= 1
                            if n == 0: # Если дошли до начала числа
                                flag = False
                                break
                        if is_simple_number(digit) == True: # Проверка цисел на простоту
                            simple_digit += 1
                        else:
                            not_simple_digit += 1
                        digit, offset_counter, counter_len_number = 0, 0, 0 # Очистка переменных,для работы с последующими числами
                    flag = True
                    mass_number.append(symbol)
                    index += 1
                    if symbol == " ": # Алгоритм поиска кол-ва чётных и нечётных ЧИСЕЛ
                        if int(mass_number[index-1]) % 2 == 0 :
                            even_digit += 1
                        else:
                            odd_digit += 1
                        break
                    elif int(symbol) % 2 == 0: # Алгоритм поиска кол-ва чётных и нечётных ЦИФР
                        even_number += 1
                    else:
                        odd_number += 1
                    symbol = file.read(symbol_len) # Читаем следующий символ

            print(f"Program time:{time.time()-start} seconds.\n")
        try:
            print("Чётных цифр ==>", round((((even_number * 100) / (even_number+odd_number))), 1), "%")
            print("Нечётных цифр ==>", round((((odd_number * 100) / (even_number+odd_number))), 1), "%\n")

            print("Чётных чисел ==>", round((((even_digit * 100) / (even_digit+odd_digit))), 1), "%")
            print("Нечётных чисел ==>", round((((odd_digit * 100) / (even_digit+odd_digit))), 1), "%\n")

            print("Простых чисел ==>", round(((simple_digit * 100) / (simple_digit+not_simple_digit)), 1), "%")
            print("Непростых чисел ==>", round(((not_simple_digit * 100) /(simple_digit+not_simple_digit) ), 1), "%")
        except ZeroDivisionError:
            print("Происходит деление на ноль..\nИли в файле нет чисел.. ")

    except FileNotFoundError:
        print("\nФайл text.txt в директории проекта не обнаружен.")

def main():
    task()

if __name__ == '__main__':
    cProfile.run("main()")
    process = psutil.Process(os.getpid())
    print(f"{(process.memory_info().rss)/(8*10**6)} MB")
