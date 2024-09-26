import time

def all(x):
    print(x.read())
    return

def stroke(y):
    for l in y.readlines():
        time.sleep(0.4)
        print(l.strip())
    return

n = input('''Введите название файла:
''')

file = open(f'{n}.txt', encoding='utf=8')

i = input('''Что вы хотите сделать с текстом?
1. Просто вывести текст
2. Вывести построчно
''')

if i == '1':
    all(file)
if i == '2':
    stroke(file)

file.close