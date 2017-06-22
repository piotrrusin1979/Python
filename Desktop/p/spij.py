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
    def oglos_przerwe(self):
        print("PRZERWA!!!!")
        
    def odpowiedz(self):
        return "To zależy :)"

class Student(Person):
    def spij(self):
        def new():
            return pytanie + " - Wszystko jasne :)"
        self.odpowiedz = new
    
        
m = Trener("Mik")
k = Person(placa=300)

m.oglos_przerwe()
s = Student("Jas")
pytanie = "Jasne?"
print(pytanie)
print(s.odpowiedz())
s.spij()
print(pytanie)
print(s.odpowiedz())
