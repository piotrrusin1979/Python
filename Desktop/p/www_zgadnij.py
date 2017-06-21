 
 
'''
   Zgadywanka liczb
'''
from bottle import route, run, template

def getRGBfromI(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return red, green, blue


import random
los = random.randint(0, 50)

print('START')

@route('/hello/')
def hello():
    return '<h1>Hello World!!!</h1>'

@route('/')
def domyslny():
    return '<h1> Witamy </h1>'
    
@route('/color/<param1>')
def listParam(param1):
    print(param1)
    if param1.isdecimal():
            param1 = int(param1)
    colorStr = str(getRGBfromI(param1))
    print(colorStr)
    return template('<body bgcolor="{{colorStr}}">', colorStr = colorStr)
    
@route('/hello/<name1>')
def index(name1):
    return template('<b>Hello {{name2}}</b>!', name2=name1)

@route('/graj/')
def graj():
    return '<h1>Podaj w adresie liczbę o której myślę.</h1>' 

@route('/graj/<nr>')
def do_graj(nr):
        if nr.isdecimal():
            nr = int(nr)
        else:
            return("<h1>LICZBE w adresie podaj !</h1>")

        if nr == los : 
            return("BRAWO !")
        elif nr > los:
            return("Za dużo.")
        else:
            return("Za mało.")


run(host='localhost', port=8080)
