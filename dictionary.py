class Dictionary:

    def __init__(self):
        self.dizionario = {}


    def addWord(self, straniera, traduzione):
        straniera_min = straniera.lower()

        if straniera_min in self.dizionario:
            self.dizionario.get(straniera_min).append(traduzione)


        elif straniera_min not in self.dizionario:
           # self.dizionario[straniera_min] = [traduzione]
            self.dizionario[straniera_min] = [traduzione]


    def translate(self, straniera):
        straniera_min = straniera.lower()
        # for i in self.dizionario.keys():
        #     if i == straniera_min:
        str = ""
        i = 0

        if straniera_min in self.dizionario:
            while i < len(self.dizionario.get(straniera_min)):
              # for i in self.dizionario.get(straniera_min):
                str += self.dizionario.get(straniera_min)[i] + " ";
                i = i + 1
        return str


    def translateWordWildCard(self, straniera):

        campi = straniera.split('?')

        temp = list(self.dizionario.keys())

        paroleTemp = []
        trad = []
        i = 0



        while i < len(temp):
            if ((campi[0].lower() in temp[i]) and (campi[1].lower() in temp[i])):

                paroleTemp.append(temp[i])
                i = i+1
            else:
                i = i+1

        if len(paroleTemp) == 0:
            return(print("Parola non trovata"))

        else:
            for i in paroleTemp:
                trad.append(self.translate(i))
        return trad





    def creaDiz(self, fileName ):
        self.fileName = fileName

        input_file = open(self.fileName, 'r', encoding='utf-8')
        riga = input_file.readline()

        while riga != "":
            campi = riga.split(" ")
            self.addWord(campi[0], campi[1])
            riga = input_file.readline()

        input_file.close()

    def __str__(self):
        listaTemp = list(self.dizionario.values())
        return print(listaTemp)
