########################################################
#    #           #            #            #     #     #            
#    ##         ##           # #            #   #      #          
#    # #       # #          #   #            # #       #        
#    #  #     #  #         #     #            #        #      
#    #   #   #   #        #########          # #       #    
#    #    # #    #       #         #        #   #      #
#    #     #     #      #           #      #      #    #
########################################################

from time import sleep
import os
import sys
import requests

user = ''
userpassword = ''
print('Начинается установка...')
sleep(1)
print('Загрузка ядра python 3.12.4')
sleep(1)
print('Загрузка графического интерфейса cmd')
sleep(1)

def install():
        print('Начата установка...')
        sleep(2)
        print('Создание регистра...')
        os.makedirs('reg')
        sleep(1)
        print('Заполнение регистра...')
        with open('reg\oslang.mreg', 'w+') as file:
            file.write(lang)
        with open('reg\primeuser.mreg', 'w+') as file:
            global user
            user = input('Необходимо создать пользователя. Введите имя: ')
            global userpassword
            userpassword = input('Введите новый пароль: ')
            file.write(f'{user}:{userpassword}')
        print('Продолжается установка...')
        sleep(1)
        print('Скачивание исполняемого файла...')
        # Укажите URL и путь, куда хотите сохранить файл
        global urlsave
        urlsave = 'https://www.dropbox.com/scl/fi/hamtez2d0nike59ieylje/Max.os.exe?rlkey=rhe3a127yzx1o6gmnjwfo2it7&st=9lmv43e7&dl=1'  # замените на вашу ссылку
        # save_path = 'Max.os.exe'  # замените на нужный путь, например, 'downloads/file.txt'
        global save_path
        save_path = 'Max.os.exe'

        # Скачиваем файл и сохраняем его
        response = requests.get(urlsave)
    
        # Проверяем, успешен ли запрос
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
        print('Установка завершена успешно, запустите файл MaxOS.exe для продолжения')
        print('Вы можете закрыть это окно')


        


        
command = ''
e = ''
lang = '0'

print('Готово, Наберите команду start для начала установки, lang для смены языка и quit для выхода из установщика')
def inpa():
    global command
    command = input('Введите команду: ')
inpa()

if command == 'quit':
    sys.exit()
elif command == 'lang':
    print('Выберите язык операционной системы, поддерживаемые языки: en-us, en-uk, ru-ru.')
    langinput = input('')
    if langinput == 'ru-ru':
        lang = '0'
        inpa()
    elif langinput == 'en-us':
        lang = '1'
        inpa()
    elif langinput == 'en-uk':
        lang = '2'
        inpa()   
    else:
        print('Введен неподдерживаемый язык, пожалуйста, повторите ввод.')
elif command == 'start':
    install()