try:
    ########################################################
    #    #           #            #            #     #     #            
    #    ##         ##           # #            #   #      #          
    #    # #       # #          #   #            # #       #        
    #    #  #     #  #         #     #            #        #      
    #    #   #   #   #        #########          # #       #    
    #    #    # #    #       #         #        #   #      #
    #    #     #     #      #           #      #      #    #
    ########################################################

    import subprocess
    
    from time import sleep
    import requests
   
    subprocess.run(['pip', 'install', 'MaxOS'], capture_output=False, text=True)
    system_app_list = ['childtasks']
    
    os_ver = '1.0.1-ex'
    import MaxOS.module
    def appinstall(app_name:str):
        if app_name == 'childtasks':
            print('Установка приложения "Задания для детей"...')
            sleep(2)
            # Укажите URL и путь, куда хотите сохранить файл
            global urlsave
            urlsave = ''  # замените на вашу ссылку
            # save_path = 'Max.os.exe'  # замените на нужный путь, например, 'downloads/file.txt'
            global save_path
            save_path = 'apps\childtasks.py'

            # Скачиваем файл и сохраняем его
            response = requests.get(urlsave)
        
            # Проверяем, успешен ли запрос
            if response.status_code == 200:
                with open(save_path, 'wb') as file:
                    file.write(response.content)

    def commandinput():
        global command, args
        commandinput1 = input(f'{part1} $ ')
        try:
            # Разделяем команду и аргументы
            split_command = commandinput1.split(" ", 1)
            command = split_command[0]  # Первая часть всегда команда
            args = split_command[1] if len(split_command) > 1 else ''  # Если есть аргументы, сохраняем их
        except Exception as e:
            print(f'Ошибка в команде: {e}')
            command = ''  # для обработки в commandwork

    def MaxOSwork():
        print('Введите команду, help для помощи, и howtostart, если вы новичок в системе')
        commandinput()
        commandwork()

    def commandwork():
        global command
        if command == 'help':
            print('Help      -           Выводит эту справку')
            print('Stop      -           Завершает работу системы')
            print('Calc      -           Считает результат с форматом: calc <num1> <operator> <num2>')
            print('Ver       -           Показывает версию OS')
            print('LibVer    -           Показывает версию библиотеки')
            print('На этом пока и всё')
            MaxOSwork()
        elif command == 'stop':
            MaxOS.module.os_stop()
            MaxOSwork()
        elif command == 'ver':
            MaxOS.module.ver('os')
            MaxOSwork()
        elif command == 'libver':
            print('Текущая версия библиотеки MaxOS: 1.1.0')
            MaxOSwork()
        elif command == 'howtostart':
            print('Это система - не как windows, а скорее как ms-dos')
            sleep(2)
            print('Она написана на языке программирования Python-3.12.4')
            sleep(2)
            print('Все команды здесь прописываются через терминал')
            sleep(2)
            print('Список команд вы можете увидеть командой help')
            sleep(2)
            print('И про будущее: в версии MaxOS-1.1.0 появится команда app, которая позволит устанавливать приложения')
            sleep(3)
            print('На этом все. Вы можете продолжать работу в системе.')
            sleep(1)
            MaxOSwork()
        elif command == 'calc':
            if args:  # Проверка наличия аргументов
                try:
                    num1, operator, num2 = args.split(" ", 2)
                    num1 = int(num1)
                    num2 = int(num2)
                    if operator == '+':
                        print(f'Результат: {num1 + num2}')
                    elif operator == '-':
                        print(f'Результат: {num1 - num2}')
                    elif operator == '*':
                        print(f'Результат: {num1 * num2}')
                    elif operator == '/':
                        if num2 != 0:
                            print(f'Результат: {num1 / num2}')
                        else:
                            print('Ошибка: Деление на ноль.')
                    else:
                        print('Введен неправильный оператор')
                except ValueError:
                    print('Произошла ошибка значения. Возможно, неправильно введена команда.')
                except Exception as e:
                    print(f'Произошла неизвестная ошибка: {e}')
            else:
                print('Ошибка: не указаны аргументы для команды calc.')
            MaxOSwork()

        elif command == 'authors':
            print('Список авторов: ')
            sleep(1)
            print('fhghfhfhfh    -    Полностью создал эту ОС')
            sleep(1)
            print('ChatGPT-4o    -    Помогала с программированием некоторых частей')
        else:
            print(f'Введена неизвестная команда: {command}. Повторите ввод')
            MaxOSwork()

    def os_load(version: str):
        import time
        print(f'Запуск MaxOS версии {version}')
        time.sleep(2)
        print('Загрузка ядра python-3.12.6')
        time.sleep(1)
        print('Загрузка графического сеанса cmd')
        time.sleep(1)
    
    password = ''
    with open('reg/primeuser.mreg', "a+", encoding='utf-8') as file:
        text = file.read()
    part1, part2 = text.split(":", 1)

    def passwordinput():
        global password
        password = input(f'Введите пароль от пользователя: {part1}: ')
        if password == part2:
            print(f'Успешный вход в систему под именем: {part1}')
            MaxOSwork()
        else:
            print('Введен неправильный пароль, повторите попытку')
            passwordinput()

    with open('reg/oslang.mreg', 'r', encoding='utf-8') as file:
        oslang = file.read()
    os_load(os_ver)
    print(f'Успешная загрузка MaxOS-{os_ver}')
    passwordinput()
except KeyboardInterrupt:
    print('Зачем вы нажали эти клавишы, не путайте меня пожалуйста')
    sleep(2)
    MaxOSwork()
# except FileExistsError:
#     print('Произошла файловая ошибка, проверьте файлы системы')
except FileNotFoundError:
    print('Произошла файловая ошибка, проверьте файлы системы.')
except Exception as exception:
    print(f'Произошла неизвестная ошибка, если вы в этом разбираетесь то вот она: {exception}')
