from steampy.guard import generate_one_time_code
import json
from tkinter import filedialog



def menu():
    print('\n Выберите действие : ', '\n 1. Список аккаунтов ', ' 2. Добавить новый аккаунт ', ' 3. Загрузить базу аккаунтов ', ' 4. Выйти', sep = '\n')
    answer = input('\n >>> ')    
    return(answer)


def acclistmenu():
    print('\n Выберите действие : ', '\n 1. Получить Steam Guard ', ' 2. Удалить аккаунт', sep = '\n')
    answer = input('\n >>> ')    
    return(answer)


def getguard():
    print('\n Введите номер аккаунта :')
    number = int(input('\n >>> ')) - 1
    with open('accounts.json') as accinfo:
        acclist = json.load(accinfo)
        sharedsecret = acclist[number]['shared']
        steamguard = generate_one_time_code(sharedsecret)
        print('\n Код Steam Guard : ', steamguard)
        
def loadaccs():
    print('\n Выберите режим : ', '\n 1. Выбрать файл ', ' 2. all_accounts.json', sep = '\n')
    answer = input('\n >>> ')
    count = 0
    if answer == '1':
        path = filedialog.askopenfilename()
        with open(path, 'r') as file:
            try:
                data = json.load(file)
                for i in data:
                    info = {
                        'name': i['account_name'],
                        'shared': i['shared_secret']
                        }
                    print(f'\n Загрузка {info["name"]} ...')
                    addacc(info)
                    count += 1
                if flag:
                    print(f'\n Успешно загружено {count} аккаунтов!')
                else:
                    pass
            except Exception as e:
                print(f'\n Ошибка чтения : {e}')
    elif answer == '2':
        with open('all_accounts.json', 'r') as file:
            print('Открытие файла...')
            try:
                data = json.load(file)
                for i in data:
                    info = {
                        'name': i['account_name'],
                        'shared': i['shared_secret']
                        }
                    print(f'\n Загрузка {info["name"]} ...')
                    addacc(info)
                    count += 1
                if flag:
                    print(f'\n Успешно загружено {count} аккаунтов!')
                else:
                    pass
            except Exception as e:
                print(f'\n Ошибка чтения : {e}')        


def addacc(info):
    global flag
    flag = True
    try:
        acclist = json.load(open('accounts.json'))
        for i in acclist:
            if info['name'] != i['name']:
                continue
            else:
                print(f'\n Аккаунт {info["name"]} уже есть в списке. Удалите его и попробуйте снова.')
                flag = False
                break
        if flag:
            acclist.append(info)
        else:
            pass
    except:
        acclist = []
    try:
        with open('accounts.json', 'w') as output:
            if flag:
                print(f'\n Аккаунт {info["name"]} был успешно добавлен!')
            else:
                pass
            json.dump(acclist, output, indent = 2, ensure_ascii = False)
    except Exception as e:
        print(f'Ошибка {e}')

        
def delacc():
    print('\n Введите номер аккаунта или напишите "+" для удаления всех аккаунтов: ')
    number = input('\n >>> ')
    if number == '+':
        with open('accounts.json', 'w') as file:
            print('', file = file)
        print('\n *Аккаунты были успешно удалены!*')
    elif number.isdigit():
        number = int(number) - 1
        with open('accounts.json', 'r') as accinfo:
            acclist = json.load(accinfo)
            print('\n Выбран аккаунт : ', acclist[number]['name'])
            answer = input(f" Напишите {acclist[number]['name']} для подтверждения удаления: \n\n >>> ")
            try:
                if answer == acclist[number]['name']:
                    with open('accounts.json', 'w') as accinfo:
                        print(f"\n Аккаунт {acclist[number]['name']} был удалён.")
                        acclist.pop(number)
                        json.dump(acclist, accinfo, indent = 2, ensure_ascii = False)
                else:
                    print('Аккаунт не был удалён. Возвращаемся.')
            except Exception as e:
                print(f'Ошибка {e}.')
    else:
        print('Ошибка ввода')

def getinfo():
    name = input('\n Введите логин аккаунта : ')
    shared = input('\n Введите shared_secret : ')
    info = {
        'name':  name,
        'shared': shared
        }
    return(info)
    
    
def acclist():
    try:
        with open('accounts.json') as acclist:
            string = json.load(acclist)
            print('\n ====================')
            print(f' Аккаунтов найдено: {len(string)}')
            for i in range(len(string)):
                print(f" | {i + 1}. {string[i]['name']}")
            print(' ====================')
            answer = acclistmenu()
            if answer == '1':
                getguard()
            elif answer == '2':
                delacc()
    except Exception as e:
        print(f' Ошибка {e}.')
        print(f' Аккаунтов найдено: 0')
        print('\n ====================')
        print(' | 1. ')
        print(' ====================')
    
while True:
    answer = menu()
    if answer == '1':
        acclist()
    elif answer == '2':
        info = getinfo()
        addacc(info)
    elif answer == '3':
        loadaccs()
    elif answer == '4':
        break
