import random


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '/', '?'] 


print('Welcome to the PY Password Generator!')

pw_letters = int(input('How many letters would you like in your password? \n'))

pw_numbers = int(input('How many numbers would you like? \n'))

pw_symbols = int(input('How many symbols would you like? \n'))


password_list = []

for char in range(0,pw_letters + 1):
    password_list.append(random.choice(letters))

for char in range(0, pw_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(0, pw_symbols + 1):
    password_list.append(random.choice(symbols))
    
print(password_list)

random.shuffle(password_list) # shuffle for do shuffle in list

print(password_list)

password = ""

for char in password_list:
    password += char

print(f'Your password is {password}')

  
   
