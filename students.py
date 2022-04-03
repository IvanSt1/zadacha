class student:
    def __int__(self):
        self.number = 0
        self.surname = ""
        self.name = ""
        self.secondname = ""
        self.room = ""
        self.ozenki = None

    def __init__(self, number, surname, name, secondname, room, ozenki):
        self.number = number
        self.surname = surname
        self.name = name
        self.secondname = secondname
        self.room = room  # номер класса
        self.ozenki = ozenki

    def vyvod(self):
        print(self.number, self.name, self.surname, self.secondname, self.room, *self.ozenki)

    def get_name(self):
        return self.name
