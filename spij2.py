'''
Po wywolaniu metody spij 
Student, nie przerywajac drzemki,
automatycznie odpowiada, ze wszystko jasne, 

'''


class Person(object):
    def __init__(self, imie="Krzys", wzrost=180, **kwargs):
        self.imie = imie
        self.wzrost = wzrost
        self.placa = kwargs.get('placa', 13)
        
    def __str__2(self):
        return str(self.__dict__)
        return "{} {}cm {}zł/h".format(self.imie, self.wzrost, self.placa)

    def __add__(self, text):
        self.imie += " " + text
        return self.imie
        
    def __lt__(self, x):
        return self.wzrost < x.wzrost
        
    def odpowiedz(self, pytanie):
        return "Nie wiem"

class Trener(Person):
    def oglos_przerwe(self):
        print("PRZERWA!!!!")
        
    def odpowiedz(self, pytanie):
        return "To zależy :)"
glob = "GLOB"
class Student(Person):
    def spij(self):
        def new(pyt):
            return  "{}: {} - Wszystko jasne :)".format(self.imie, pyt)
        new.__name__ = 'odpowiedz'
        self.odpowiedz = new#.__call__
    
        
m = Trener("Mik")
k = Person(placa=300)

m.oglos_przerwe()
s = Student("Jas")
pytanie = "Jasne?"
print(pytanie)
print(s.odpowiedz(pytanie))
s.spij()
print(pytanie)
print(s.odpowiedz(pytanie))