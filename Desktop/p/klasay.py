class Person(object):
    def __init__(self, imie="Krzys", wzrost=180, **kwargs):
        self.imie = imie
        self.wzrost = wzrost
        self.placa = kwargs.get('placa', 13)
        
    def __str__(self):
        return str(self.__dict__)
        return "{} {}cm {}zł/h".format(self.imie, self.wzrost, self.placa)

    def __add__(self, text):
        self.imie += " " + text
        return self.imie
        
    def __lt__(self, x):
        return self.wzrost < x.wzrost
        
    def odpowiedz(self):
        return "Nie wiem"

class Trener(Person):
    def __init__(self, coUmie, imie="Krzys", wzrost=180, **kwargs):
        self.coUmie = coUmie
        super(Trener, self).__init__(imie, wzrost)

    def oglos_przerwe(self):
        print("PRZERWA!!!!")
        
    def odpowiedz(self):
        return "To zależy :)"


T1 = Trener("Fizyka")
T2 = Trener("Math", imie="wojtek", wzrost=500)
