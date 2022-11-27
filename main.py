#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91p
password = []
total_char = nr_letters + nr_symbols + nr_numbers
length_letters = len(letters)
length_numbers = len(numbers)
length_symbols = len(symbols)

for i in range(0, nr_letters):
  rand_idx = random.randint(0, length_letters - 1)
  rand_letter = letters[rand_idx]
  password.append(rand_letter)

for i in range(0, nr_symbols):
  rand_idx = random.randint(0, length_symbols - 1)
  rand_symbol = symbols[rand_idx]
  password.append(rand_symbol)

for i in range(0, nr_numbers):
  rand_idx = random.randint(0, length_numbers - 1)
  rand_number = numbers[rand_idx]
  password.append(rand_number)

# Origin pass
pass_str = ""
for c in password:
  pass_str += c
print(password)

# Random pass
random.shuffle(password)
randPass_str = ""
for c in password:
  randPass_str += c
print(password)
print(f"Your password is: {randPass_str}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P