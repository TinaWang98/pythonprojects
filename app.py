# print('I am Tina')
#
# #Variables
# price = 10
# rating = 4.9
# name = 'Tina'
# is_published = True
# print(price)
# patient_name = 'John Smith'
# patient_age = 20
# is_new_patient = True

#Getting Input
# name = input('What is your name? ')
# fav_color = input('What is your favourite color? ')
# print(name + ' likes ' + fav_color)

#Type Conversion
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2023 - int(birth_year)
# print(type(age))
# print('My age is ' + str(age))
#Exercise
# weight_lbs = input('Your weight(lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print('Your weight in Kg is: ' + str(weight_kg))

#String
# course = 'Python for Beginners'
# another = course[:]
# print(course[0])
# print(course[-2])
# print(course[0:3])
# print(course[:5])
# print(another)
# name = 'Jennifer'
# print(name[1:-1])
# print(name[1:7])

#Formatted Strings
# first = 'John'
# last = 'Smith'
# msg = f'{first} [{last}] is a coder'
# print(msg)

#String Methods
# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course)
#
# print(course.replace('n','A'))
# print('python' in course)
# print(course.title())

#Arithmetic Operations
# x = 10
# x *= 3
# print(x)

#Operator Precedence
# x = (10 + 3) * 2 ** 2
# print(x)

#Math Functions
# import math
# x = 2.9
# print(math.ceil(2.9))
# print(math.floor(2.9))
# # print(round(x))
# # print(abs(-2.9))

#If Statements
# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")
#Exercise
# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_payment = price * 0.1
# else:
#     down_payment = price * 0.2
# print(f"Down payment: ${down_payment}")

#Logical Operators
# has_high_income = True
# has_good_credit = True
# has_criminal_record = False
#
# if has_good_credit and not has_criminal_record:
#     print("Eligble for loan")

#Comparison Operators
# temperature = 30
# if temperature != 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")
# name = input("Your name: ")
# length = len(name)
# if length < 3:
#     print("name must be at lease 3 characters")
# elif length > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good")

#Project: Weight Converter
# weight = input('Weight: ')
# unit = input('(L)bs or (K)g: ')
# if unit.lower() == 'l':
#     print(f'You are {int(weight) * 0.45} kilos')
# else:
#     print(f'You are {int(weight) / 0.45} pounds')

#While Loops
# i = 1
# while i <= 5:
#     print('*'* i)
#     i = i + 1
# print("Done")

#Guessing Game
# guess_count = 1
# guess_limit = 3
# while guess_count <= guess_limit:
#     input_number = int(input('Guess: '))
#     guess_count += 1
#     if input_number == 9:
#         print('You win!')
#         break
# else:
#     print("You have failed")

#Car Game
# started = False
# stopped = False
# while True:
#     command = input('> ').lower()
#     if command == 'help':
#         print('''
#         start - to start the car
#         stop - to stop the car
#         quit - to quit
#         ''')
#     elif command == 'start':
#         if not started:
#             started = True
#             print('Car started...Ready to go!')
#         else:
#             print('Car has already started!')
#     elif command == 'stop':
#         if not stopped:
#             stopped = True
#             print('Car stopped.')
#         else:
#             print('Car has already stopped')
#     elif command == 'quit':
#         print('Exit')
#         break
#     else:
#         print("I don't understand that...")

#For Loops
# prices = [10, 20, 30]
# total_cost = 0
# for price in prices:
#     total_cost += price
# print(total_cost)

#Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

#Challenge
# numbers = [2, 2, 2, 2, 5]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

#Lists
# names = ['John', 'Bob', 'Mosh', 'Sarah']
# names[0] = 'Jon'
# print(names)

#Exercise
# numbers = [3, 6, 2, 8, 4, 10]
# max = 0
# for num in numbers:
#     if num > max:
#         max = num
# print(max)

#2D Lists
# matrix = [[1, 2, 3], [4, 5, 6]]
# for row in matrix:
#     for item in row:
#         print(item)

#List Methods
# numbers = [5, 2, 1, 7, 4, 5]
# numbers2 = numbers.copy()
# print(numbers.append(20))
# print(numbers2)

#Exercise
# numbers = [5, 2, 1, 7, 4, 5, 2, 2]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

#Tuples
#immutable
# numbers = (1, 2, 3)
# print(numbers[0])

#Unpacking
# coordinates = [1, 2, 3]
# x, y, z = coordinates
# print(y)

#Dictionaries
#key value pairs
# customer = {
#     "name": "John",
#     "age": 30,
#     "is_verified": True
# }
# customer["birthdate"] = "Jan 1 1980"
# print(customer.get("birthdate"))

#Exercise
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# input_phone = input("Phone: ")
# output = ""
# for ch in input_phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)

#Emoji Converter

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😃",
#         ":(": "😞"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
# print(emoji_converter("Good morning :)"))


#Functions
#Parameters
#Keyword Arguments
# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aborad")
#
#
# print("Start")
# greet_user("Tina", "Wang")
# print("Finish")

#Return Statements
# def square(number):
#     return number * number
#
# result = square(3)
# print(result)

#Exceptions
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0')
# except ValueError:
#     print('Invalid value')

#Classess











