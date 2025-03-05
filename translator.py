import dictionary as dr
class Translator:


    def __init__(self):
        self.d = dr.Dictionary()



    def printMenu(self):
        print(f"1. Aggiungi nuova parola")
        print(f"2. Cerca una traduzione")
        print(f"3. Cerca con wildcard")
        print(f"4. Stampa tutto il dizionario")
        print(f"5. Exit")


    def loadDictionary(self, dict):
        self.d.creaDiz(fileName = dict)
        # dict is a string with the filename of the dictionary


    def handleAdd(self, entry):
        campi = entry.split(" ")
       # if (len(campi) == 2):

        i = len(campi)
        j = 1;
        if i == 2:
         self.d.addWord(campi[0], campi[1])
        else:
            while j < i:
                self.d.addWord(campi[0], campi[j])
                j = j+1
        # else:
        #     i = len(campi)
        #     j = 0
        #     while(j != i):
        #         self.d.addWord(campi[0], campi[j])
        #         j = j +1


        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

        print(f"Aggiunta!")


    def handleTranslate(self, query):
        print(self.d.translate(query))
        # query is a string <parola_aliena>


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        print(self.d.translateWordWildCard(query))

    def stampaDizionario(self):
        return self.d.__str__()
