import re
try:
    print("\n ___  Результат работы программы  ___ \n")
    with open('laboratornaya2.txt', 'r') as file:
        buffer = file.read()
        if not buffer:
            print('\nРабочий файл пустой, измените содержание файла')
        if re.findall(r'"[\w*\s]{0,}\S"', buffer):
            work_buffer = re.findall(r'"[\w*\s]{0,}\S"', buffer)
            print(work_buffer)
        else:
            print('В файле laboratornaya2.txt отсутствуют цитаты.\nОтредактируйте файл и запустите программу заново.')
except FileNotFoundError:
    print('\nФайл laboratornaya2.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий')