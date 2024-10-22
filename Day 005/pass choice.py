import random

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '#', '$', '%', '&', '(', ')', '*', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Viki Password Generator!")
nr_chars = int(input("How many characters would you like in your password?\n"))

password_list = []
random.shuffle(chars)
for char in range(0, nr_chars):
    password_list += random.choice(chars)

password = ""

for i in password_list:
    password += i

print(f"Your password is {password}")
