import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Quale parola devo aggiungere?")
        txtIn = input()
        t.handleAdd(txtIn)

    elif int(txtIn) == 2:
        print("Quale parola devo tradurre?")
        txtIn = input()
        t.handleTranslate(txtIn)

    elif int(txtIn) == 3:
        print("Quale parola devo tradurre?")
        txtIn = input()
        t.handleWildCard(txtIn)

    elif int(txtIn) == 4:
        print("Stampo il dizionario")
        t.stampaDizionario()

    elif int(txtIn) == 5:
        break