word = "белка"
print("Добро пожаловать в игру! Перед вами зашифрованное слово, вы должны вводить буквы и отгадывать его. Подробнее о правилах игры узнайте с помощью команды helpme")
gamepad = "*" * len(word)
myenters = set()
alphabet = "йцукенгшщзхъфывапролджэёячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТЬБЮ"
helpme = "mywins - буквы, введенные мной и сопадающие с какой-либо буквой из загаданного слова" + "\n" + "myenters - буквы, которые я вводил" + "\n" + "giveup - сдаться"
mywins = set()
commands = set()
commands.add("helpme")
commands.add("myenters")
commands.add("mywins")
commands.add("giveup")
print(gamepad)
attempts = len(word) * 2
while attempts > 0:
    ent = input() 
    if ent in commands:
        if ent == "mywins":
            for elem in mywins:
                print(elem, end=" ")
            print("\n")
        if ent == "helpme":
            print(helpme)
        if ent == "myenters":
            for elem in myenters:
                print(elem, end=" ")
            print("\n")
        if ent == "giveup":
            print(len(myenters), "попыток")
            print("ВЫ ПРОИГРАЛИ")
            print("загаданное слово:", word)
            break
        attempts += 1
    elif ent == word:
        print(len(myenters), "попыток")
        print("ПОБЕДА")
        gamepad = word
        break 
    elif ent in myenters:
        print("такую букву вы уже пробовали")
    elif ent in word:    
        print("верно!!!")
        letter = 0
        while word[letter] != ent:
            letter += 1
        gamepad = gamepad[:letter] + ent + gamepad[letter + 1:]
        myenters.add(ent)
        mywins.add(ent)
        if gamepad == word: 
            print(len(myenters), "попыток")
            print("ПОБЕДА")
            break
    elif ent in alphabet and ent not in word:
        print("неверно")
        myenters.add(ent)
    else:
        print("ОШИБКА")
    print(gamepad)
    attempts -= 1
    print("осталось попыток:", attempts)
print(word)
if gamepad != word and ent != "giveup":
   print("ПРОИГРЫШ")
   print("загаданное слово:", word) 