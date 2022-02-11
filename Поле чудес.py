import random # модуль рандом, узнал из интернета. Источник: https://clck.ru/au7sA

print(" " * 26 + "ЗДРАВСТВУЙ ДОРОГОЙ ИГРОК!") #приветствие
print(" " * 26 + "Я ВИРТУАЛЬНЫЙ ЯКУБОВИЧ 2079")
print(" " * 26 + 'ПРИВЕТСТВУЮ НА ИГРЕ "ПОЛЕ ЧУДЕС"')
print(" " * 26 + "АВТОР ИГРЫ - ДАНИСИМУС")
print(" " * 26 + "УЗНАТЬ СПИСОК КОМАНД - !список команд")

bukvi = "абвгдеёжзийклмнопрстуфхцчъыьэюя" #алфавит
popitki = 1 #попытки
spisok = ["лицензия", "ординатура", "юриспруденция", "водонагреватель", "доброжелательность", "религиовед", "вероисповедование", "гастарбайтер", "достопримечательность", "человеконенавистничество", "автостеклоподъемники", "конфорка", "якубович"] #список слов
random_slovo = list(random.choice(spisok)) #загаданное слово

zvezdi = list("*" * len(random_slovo)) #зашифрованное слово
print("Слово:")
print(*zvezdi, sep="") #первый вывод шифра

while True: #Раунд
    if "*" not in str(zvezdi): #Если все буквы поочерёдно введены
        print("ПОБЕДА!!! Слово угадано")
        print("Попытки:", popitki)
        break
    bukva_or_slovo = input("Введите букву или слово:").lower() #Ввод буквы или слова
    if ((bukva_or_slovo not in bukvi and len(bukva_or_slovo) == 1) or (len(bukva_or_slovo) != 1 and len(bukva_or_slovo) != len(random_slovo))) and bukva_or_slovo[0] != "!": #проверка корректности ввода
        print("Мне кажется, или это не буква и не слово?")
    elif list(bukva_or_slovo) == random_slovo: #Если игрок ввёл слово
        print("ПОБЕДА!!! Это был трудный путь, но вы справились")
        print("Попытки:", popitki)
        break
    # Если игрок угадал букву
    elif bukva_or_slovo in random_slovo and bukva_or_slovo not in zvezdi: 
        print("Вы угадали!!!")
        for indexx in range(len(random_slovo)): #замена звёзд на буквы в шифре
            if bukva_or_slovo == random_slovo[indexx]:
                zvezdi[indexx] = bukva_or_slovo
    elif bukva_or_slovo in zvezdi: #если игрок ввёл букву, которую уже вводил
        print("Вы уже называли такую букву")
    elif bukva_or_slovo[0] == "!": #команды
        if bukva_or_slovo == "!сдаться": #команда, чтобы сдаться
            print("Вы уверены?")
            print("Если да, напишите 'Да', если нет, напишите 'Нет'")
            if input().lower() == "да": #подтверждение
                print("Вы сдались")
                print("Загаданное слово:", *random_slovo, sep="")
                break
        if bukva_or_slovo == "!список команд": #вывод списка команд
            print("КОМАНДЫ:")
            print("!сдаться - СДАТЬСЯ")
            print("!правила игры - ПРАВИЛА ИГРЫ")
            print("!попытки - ПОПЫТКИ")
        if bukva_or_slovo == "!попытки": #вывод попыток
            print(popitki)
        if bukva_or_slovo == "!правила игры": #вывод правил игры
            print("ИГРА 'ПОЛЕ ЧУДЕС'")
            print("Загадывается слово и шифруется звёздочками")
            print("Ваша задача отгадать слово")
            print("В один ход можно назвать букву или слово целиком")
            print("Игра не закончится пока вы не угадаете слово или пока вы не сдадитесь")
    else: #если введена неправильная буква
        print("Не угадали")
        popitki += 1
    print("Слово:")
    print(*zvezdi, sep="") #второй и последующий ввод шифра
    