from keyboard import write, send, wait
from random import randint
from sys import stdin
from time import sleep

ch = int(input('1 Обычный режим\n2 Режим спама\nВведите режим: '))
key = input('Введите клавишу перед вводом в чат (необ.): ')

if ch == 1:
    print("Введите текст (Ctrl+Z, а затем enter для завершения)")
    text = stdin.read().split()
    a = float(input('Введите задержку сообщений (в секундах): '))
    x, y = map(int, input('рандом слов от x до y (1 10): ').split())
    print('Нажмите ` для начала, Ctrl + Z в консоли для завершения')
    wait('`')
    while text:
        i = randint(x, y)
        if key:
            send(key)
        write(' '.join(text[:i]), delay=a)
        send('enter')
        del text[:i]

elif ch == 2:
    p = int(input('Введите кол-во повтрений: '))
    print('\n\nСкопируйте нужный текст!\nНажмите ` для начала, Ctrl + Z в консоли для завершения')
    wait('`')
    for el in range (p):
        if key:
            send(key)
        send('ctrl+v')
        sleep(0.1)
        send('enter')
