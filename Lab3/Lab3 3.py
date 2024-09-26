import time

while True:
    try:
        name = input('Введите название файла:\n')
        file = open(f'{name}.txt', encoding='utf=8')
        i = input('Что вы хотите сделать с текстом?\n1. Просто вывести текст\n2. Вывести построчно\n')
        if i == '1':
            print(file.read())
        if i == '2':
            for l in file.readlines():
                time.sleep(0.4)
                print(l.strip())
        file.close()
        break

    except FileNotFoundError:
        i = input(
            'Такого файла не существует, хотите создать новый файл?\n1. Создать новый файл\n2. Ввести название заново\n')
        if i == '1':
            name = input('Введите название файла:\n')
            file = open(f'{name}' + '.txt', 'a+', encoding='utf=8')
            text = input('Введите текст для файла:\n')
            file.write(f'{text}\n')
            file.close()
            break