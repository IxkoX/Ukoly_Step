# user.py

import os, json


DATA_PATH = 'Ukoly_Step/Ukol_01/users.json'

def read_data():
    with open(DATA_PATH, encoding='utf-8') as file:
        return json.load(file)
    
def write_data(data):
    with open(DATA_PATH, mode="w", encoding='utf-8') as file:
        json.dump(data, file) #zapiš to do json

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError('Hesla se neshodují')
    
def check_username(data, username):
    if username in data:
        raise ValueError('Uživatel již existuje')

def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()
    check_username(username, data) 
    data[username] = password
    data = write_data(data)

def login(username, password):
    data = read_data()
    try: 
        assert data[username] == password, 'Chybné heslo'
        return True
    except (KeyError, AssertionError):
        return False

def logout(username):
    pass

def change_password(username, old_password, password, password_repeat):
    data = read_data()
    if username in data and data[username] == old_password:
        check_password(password, password_repeat) 
        data[username] = password 
        write_data(data)
    else:
        raise ValueError('Nesprávné uživatelské jméno nebo heslo')

    

def delete_user(username, password):
    data = read_data()
    if username in data and data[username] == password:
        del data[username]
        write_data(data)


#register('test4', 'heslo', 'heslo')
#print(login('tes', 'heslo'))
#delete_user('test4','heslo')
change_password('test2', 'heslo2','heslo1','heslo1')
