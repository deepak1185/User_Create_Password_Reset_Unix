#password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= 11
nr_symbols= 3
nr_numbers= 4

string = ""
def password_string(characters, length):
    global string
    for char in characters:
        string = random.sample(characters, length)
        return string
letter_string = password_string(letters, nr_letters)
number_string = password_string(numbers, nr_numbers)
symbol_string = password_string(symbols, nr_symbols)
final_string = (letter_string + number_string + symbol_string)
#print(final_string)
random.shuffle(final_string)
final_password = ""
for char in final_string:
    final_password += char
print(final_password)

