# pip install cryptography Required or
# pip3 install cryptography or 
# python -m pip install cryptography
# https://cryptography.io/en/latest/fernet/ #forum

# from typing_extensions import Required # its works 

from cryptography.fernet import Fernet # Biblioteca não funciona ainda



'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# master_pwd = input("What is the master password? ")
key = load_key() # + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "Password:", fer.decrypt(passw.encode()))

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or wiew existing ones(view, add), press Q to quit? ").lower()
    if mode == "q":
        pass

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.") 
        continue

# Credits: Tech with tim - Youtube
