import os
import re
import time

work_buffer = ''
fin_buffer = ''
bufferl = ''
buffer_len = 1
flag = False
flag2 = False
h = 0
try:
    print("\n ___  Результат работы программы  ___ ")
    print("\n ___  Локальное время", time.ctime()," ___ \n")
    with open('laboratornaya2.txt', 'r') as file:   #открываем файл
        buffer = file.read(buffer_len)  #считываем символ из файла
        start = time.time()
        if not buffer:
            print('\nРабочий файл пустой, измените содержимое файла')   #если в файле нет символов
        while buffer:
            if re.findall(r'["]', buffer) and not flag2:    #поиск ковычек
                work_buffer += buffer   #запись конечного результата
                buffer = file.read(buffer_len)  #чтение следующего символа
                flag = True
                flag2 = True
                h += 1
            if re.findall(r'[\w\s\S,;:^"]', buffer) and flag:   #вывод всех символов после ковычек
                work_buffer += buffer
            if re.findall(r'["]', buffer) and flag: #поиск последних ковычек в цитате
                h += 1
                work_buffer += buffer
                if re.findall(r'"\s*"', work_buffer):
                    work_buffer = re.sub('"\s*"', 'a', work_buffer[:-1])
                if work_buffer == 'a':
                    bufferl = bufferl
                else:
                    bufferl = work_buffer
                    print(bufferl)
                bufferl = ''
                work_buffer = ""    #обнуление конечной переменной
                flag = False
                flag2 = False
            buffer = file.read(buffer_len)    #чтение следующего символа
        finish = time.time()
        result = finish - start
        if h == 0:   #проверка на наличие ковычек
            print('\nВ тексте отсутствуют цитаты.')     #вывод в случае отсутствия ковычек
        if h % 2 == 1:
            print('\nВ тексте присутствуют неполные цитаты, отредактируйте текст.')
        print("\nProgram time: " + str(result) + " seconds.")
        print("Program size: " + str(os.path.getsize('laba2.py')) + " bytes.")
except FileNotFoundError:
    print('\nФайл laboratornaya2.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий')     #вывод в случае если нет файла
