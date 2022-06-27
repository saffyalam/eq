# working with String#-------------------------

# character_name = " Safwan"
# character_age = "30"
#
# print ("There was once a man named" + character_name )
# print ("He was " + character_age + " years old")
# print ("He really liked the name " + character_name)
# print ("But did'nt like being " + character_age)

# print("Aptos\nCanada")
# phrase = "Giraffe Academy"
# print(phrase + " is cool")
#
# print (phrase.upper())
#
# print (len(phrase))
#
# print(phrase[2])
#
# print(phrase.index("emy"))
#
# print (phrase.replace("Giraffe","Kutta"))


# Working with numbers#--------------

# print(3*4)
# print(10%3)
# print(-2.09)
#
# my_num= 2.098
# print(str(my_num) + " my favorite number")
# print(my_num +"is my favorite number")

# functions #-------------------
# my_num = -5
# print(abs(my_num))
# print(pow(3,2))
# print(round(3.7))
#
# from math import *  #gives more math function#
#
# print(floor(3.2))
# print(sqrt(36))

#- Getting input from user #--------------

# name = input("Enter your name: ")
# print("Hello " + name + "!")
# age = input("Enter your age: ")
# print("You are " +age+ " years old")

# name = input("What is your name? ")
# print("Hello " +name+ "!! Welcome to the house")
# age= input("your age is? ")
# if age <= str(30):
#     print("Your pretty young")
# else:
#     print("not bad")



# Building a calculator #----------------
#
# num1 = input("Enter 1st number: ")
# num2 = input("Enter 2nd number: ")
# result = int(num1) + int(num2)
# # result = float(num1) + float(num2)
# print(result)

# Madlibs GAME #------------------------------
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter celebrity: ")
#
# print("Roses are " + color)
# print(plural_noun + " are BLUE")
# print("I Love " + celebrity)
#



# # Working with List #------------------
# friends = ["Safwan", "Shaiq", "Sifat"]
# print (friends)
# print (friends[2])
# print (len(friends))

# List functions #-------------

# numbers = [4, 8, 15, 16, 23, 42]
# friends = ["Safwan", "Shaiq", "Sifat", "Yasin", "Arafat"]
# print(friends.extend(numbers))

# print(friends)
# friends.append("Rafi")
#
# friends2 = friends.copy()
# print (friends2)
#
# friends.insert(1, "Kalam")
# friends.remove("Shaiq")
#
# print (friends)
#
# print(friends.index("Yasin"))



# Tuples #-----------------

# coordinates = (4,5)
# print(coordinates)
# print(coordinates[1])

# Functions #-------------

# def  say_hi():
#     print("Hello User")
#
#
# say_hi()
# print("Kutta")

# def say_hi(name, age):
#     print("Hello "+ name)
#     print("You are " + str(age) +" years old")
#
# say_hi("Safwan", 30)

# Return Statement #-------------------

# def cube(num):
#      return pow(num, 3)
#      #return num*num*num
#
# print(cube(3))
#
# result = cube(4)
# print(result)


# If statement #---------------
#
# is_male = False
# is_tall = False
#
# if is_male and is_tall:
#     print("You are a male or tall or both")
#
# else:
#     print("You are female or short or both")
#

# is_male = False
# # is_tall = True
# #
# # if is_male and is_tall:
# #     print("You are a male and tall person")
# # elif is_male and not(is_tall):
# #     print("You are male and short person")
# # elif not(is_male) and is_tall :
# #     print("Your are female and tall")
# # else:
# #     print("You are female person")


# ------------------if comparison #-----------------

# def max_num(num1,num2,num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
#
# print(max_num(1000,50,60))

# ----------------Advanced calculator---------------
#
# num1 = float(input("Enter first number: "))  #converts the input ingto float number
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print (num1 * num2)
# else:
#     print("invalid operator")


# #-----Dictionaries #---------------

# monthconversions = {
#     "Jan" : "January",
#     "Feb" : "February",
#     "Mar" : "March",
#     4 : "April",
#
# }
#
# print(monthconversions.get("Jan"))
# print(monthconversions[4]) #monthconversions.get("LUV") could also be used


# car = {
#     "manufacturer":"honda",
#     "model":"accord",
#     "year":2015,
#     "price": 17000
# }
#
# print(car.get("model"))

#-----------_While loop---------------------#

# i = 7
# while i <= 10:
#     print(i)
#     i = i+1
# print("Loop completed")


#------------Guessing Game-------------#

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_off_guesses = False
#
# while guess != secret_word and not(out_off_guesses):
#     if guess_count < guess_limit:
#         guess = input ("Enter guess: ")
#         guess_count = guess_count + 1
#     else:
#         out_off_guesses = True
# if out_off_guesses:
#     print("You are out of guess")
# else:
#
#     print ("Your guess is right!!!")



#

#
# secret_number = 777
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guess= False
#
# while guess != secret_number and not(out_of_guess):
#     if guess_count < guess_limit:
#         guess = float(input("Enter guess: "))
#         guess_count += 1
#     else:
#         out_of_guess = True
#
# if out_of_guess:
#     print("Out of guess. You lost!!")
#
# else:
#     print("You guessed correct number")
#


#----------------For loop---------#

#
# for letter in "Giraffe Academy":
#     print(letter)  #loops and prints every letter#
#

# friends = ["Jimmy", "Kalla Bomba", "Ayaz"]
#
# for letter in friends :
#     print(letter)
#
# for index in range(5) :
#     if index == 0:
#         print("First Iteration")
#     else:
#         print ("Not first iteration")


#--------_Exponent Function-------------_#

# print(pow(2,3))
# print(2**3)
# #
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print (raise_to_power(2,3))


#-------2D list and nested LOOP-----#

# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
#
# print(number_grid[2][1])
#
# print (number_grid)
#
# for row in number_grid:
#     print(row)
# for row in number_grid:
#     for col in row:
#       print (col)


#-----------Build a translator--------------#

#vowels-> g
#e.g: dog->dgg

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#
#     return translation
#
# print(translate(input("Enter a phrase: ")))



#----------Comments----------_#

#print ("Print  # comments or fun")

# comment

'''
sadddy

'''

#------Exception catc---#
#
# try:
#     value= 10/2
#     print (int(value))
#
#     number = int(input("Enter a number: "))
#     print (number)
# except ValueError:
#     print("Invalid input format")
# except ZeroDivisionError:
#     print("DIVIDED BY ZERO")


#---------Writing or Reading Files-----------#

# employee_file = open("untitled", "r")
# for employee in employee_file.readline()
#  # print(employee_file.readable())
# employee_file.close()
#
# employee_file = open("Untitled", "r")
# print(employee_file.read())
# employee_file.close()
#
# employee_file = open("Untitled", "a")
# employee_file.write("\nKallaBOMBA")
# employee_file.close()
#
# #-----------Module and PIP---------#
# import bill
#
# print(bill.cube(3))
#
#
#







