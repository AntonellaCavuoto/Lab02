class Dictionary:

    def __init__(self):
        self.dizionario = {}


    def addWord(self, straniera, traduzione):
        straniera_min = straniera.lower()
       # for i in self.dizionario:
        if straniera_min in self.dizionario:
            self.dizionario[straniera_min].append(traduzione)

        else:
            self.dizionario[straniera_min] = [traduzione]


    def translate(self, straniera):
        straniera_min = straniera.lower()
        # for i in self.dizionario.keys():
        #     if i == straniera_min:
        str = ""
        if straniera_min in self.dizionario:
            for i in self.dizionario.get(straniera_min):
                str += i
                return str


    def translateWordWildCard(self):
        pass

    def creaDiz(self, fileName ):
        self.fileName = fileName

        input_file = open(self.fileName, 'r', encoding='utf-8')
        riga = input_file.readline()

        while riga != "":
            campi = riga.split(" ")
            self.addWord(campi[0], campi[1])
            riga = input_file.readline()

        input_file.close()