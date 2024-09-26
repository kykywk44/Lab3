w = open('user_input.txt','a+')

i = input('Ваш текст: \n')
w.write(f'{i}\n')

w.close()

