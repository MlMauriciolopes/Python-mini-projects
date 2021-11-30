#
import random

chars = "abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVXWYXZ0123456789!@#$%&*"

while 1:
    password_len = int(input("What length would you like your password to be: ")) # número de caracteres
    password_count = int(input("How many passwords would like: ")) # variações

    for count in range(0, password_count):
        password = ""
        for count in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password: ", password)