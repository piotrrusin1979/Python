# https://regex101.com/

import re

text = "123\n222\n22422\n555\n42\nend"
wyszukiwaczka = re.compile(r'42')
wynik = wyszukiwaczka.findall(text)
print(wynik)

wzor = r'\w+[-\s]+\d{4}'
wyszukiwaczka = re.compile(text)
text="Szkoleniez PYTHON-2010"
if wyszukiwaczka.search(text):
    print("OK")
    
text = "Ala ma kota. Kot ma Alę. Ala nie ma psa.\nAla ma jaszczurkę. Al nie ma psa.\n\nAlicja to imie Ali."
wzor = r' Ala ma PYTHON-()'
wyszukiwaczka = re.compile(wzor)

wynik = wyszukiwaczka.findall(text)
print(wynik)

wyszukiwaczka = re.compile(r'ma (?P<pk>[a-z]+)')
wynik = wyszukiwaczka.search(text)
print(dir(wynik))
print(wynik, wynik.group())

text = "Ala ma kota. Kot ma 3 Ale. Ala nie ma psa.\nAla ma jaszczurkę. 42 to odpowedz.Al nie ma psa.\n\n 22Alicja to imie Ali."
wyszukiwaczka = re.compile(r'ma (?P<pk>[a-z]+)')
wynik = wyszukiwaczka.findall(text)
print(wynik)

