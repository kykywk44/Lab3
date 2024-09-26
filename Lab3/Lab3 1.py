import time

n = input('Введите название файла:\n')

file = open(f'{n}.txt', encoding='utf=8')

i = input('''Что вы хотите сделать с текстом?
1. Просто вывести текст
2. Вывести построчно
''')

if i == '1':
    print(file.read())
if i == '2':
    for l in file.readlines():
        time.sleep(0.4)
        print(l.strip())

file.close
