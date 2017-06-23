'''
Jak zrobić API Restfull
(install Git with Unix tools, Windows 7)

c:\Mikolaj>curl -X GET  http://localhost:8080/los
{"los": 11}
c:\Mikolaj>curl -X GET -H "Content-Type: application/json"   http://localhost:8080/los
{"los": 15}

c:\Mikolaj>curl -X POST -H "Content-Type: application/json" -d "{ \"los\": \"17\" }"  http://localhost:8080/file
{"17": 14}

https://youtu.be/BHAUJUuhiDw?list=PLQgaiFtVuv4aJ0A24HEGosxw0NeTCH7P2

'''
from bottle import run, get, post, delete, request

import random
import fnmatch
import os

print('START')

@get('/los')
def losuj():
    los = random.randint(0, 50)
    return {'los': los}

@get('/file')
def get_all():
    files = [x for x in os.listdir(r'.') if fnmatch.fnmatch(x,'*.los')]
    return {'files': files}    

@get('/file/<name>')
def get_one(name):
    with open(name + ".los", "r+") as f:
        return {'file': f.read() if f is not None else 'ni ma ' + name}    

@delete('/file/<name>')
def delete_one(name):
    os.remove(name)
    return {'deleted_file': name}    
        
@post('/file')
def add_one():
    los = request.json.get('los')
    with open(los + ".los", "a+") :
        pass    
    # f = open(los,'a'); f.close(); 
    with open(los + ".los", "r+") as f:
        lines = f.readlines()
        ile = 1 if not lines or not lines[0].strip().isdecimal() else int(lines[0].strip()) + 1
        f.seek(0)
        print(ile)
        f.write(str(ile)+"\n")
    print("I got POSTed {} number {} time.".format(los, ile))
    return {los: ile}
    



run(host='localhost', port=8080, debug=True ) # , reloader=True)