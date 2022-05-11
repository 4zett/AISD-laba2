import re
work_buffer = ''
fin_buffer = ''
buffer_len = 1
flag = False
flag2 = False
h = 0
try:
    print("\n ___  Результат работы программы  ___ \n")
    with open('laboratornaya2.txt', 'r') as file:
        buffer = file.read(buffer_len)
        if not buffer:
            print('\nРабочий файл пустой, измените содержание файла')
        while buffer:
            if re.findall(r'["]', buffer) and not flag2:
                work_buffer += buffer
                buffer = file.read(buffer_len)
                flag = True
                flag2 = True
                h += 1
            if re.findall(r'[\w\s\S,;:^"]', buffer) and flag:
                work_buffer += buffer
            if re.findall(r'["]', buffer) and flag:
                work_buffer += buffer
                print(work_buffer[:-1])
                work_buffer = ""
                flag = False
                flag2 = False
            buffer = file.read(buffer_len)
        if h == 0 and buffer:
            print('\nВ тексте отсутствуют цитаты.')
except FileNotFoundError:
    print('\nФайл laboratornaya2.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий')