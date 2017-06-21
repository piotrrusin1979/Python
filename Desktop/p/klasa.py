class Mojaklasa(object):
    def __init__(self, imie="krzys", wzrost=180, **kwargs):
        self.imie = imie
        self.wzrost = wzrost
        self.placa = kwargs.get("placa", 13)
    def __add__(self, text):
        self.imie += "" +text
        return self.imie
    def __str__(self):
        return ("imie {0}, wzrost {1}, płaca {2}".format(self.imie, self.wzrost, self.placa))
    
    def __repr__(self):
        return "Mojaklasa('{}',{},placa={})".format(self.imie, self.wzrost, self.placa)
    
        
        

m = Mojaklasa()
print(m)
print(repr(m))