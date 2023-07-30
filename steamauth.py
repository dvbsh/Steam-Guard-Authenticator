from steampy.guard import generate_one_time_code as gencode
import json

shared_secret = input('Введите shared_secret : ')

while True:
    print('Напишите "+" для получения Guard или "-" для выхода из программы')
    answer = input()
    if answer == '+':
        code = gencode(shared_secret)
        print('Код Steam Guard :', code)
    elif answer == '-':
        break
