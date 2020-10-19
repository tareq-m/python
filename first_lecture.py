# Exercises

# Strings
# Exercise (Easy)
# Ask the user for his name, and then print a greeting message

# -------->    ANSWER  <-----------

# user_name = input('Enter name Please: ')
# print(f"How are you" ,user_name,)
 
# Exercise (Easy)
# Ask two users for their names, and then tell them who got the longest name.

# -------->    ANSWER  <-----------

# first_user = input('First user name: ')
# second_user = input ('Second user name: ')

# if len(first_user) > len(second_user) :
#     print(f'your name is longer',first_user,)
# else :
#     print(f'your name is longer',second_user,)

# Exercise (Easy)
# Ask a user for his name, and if it starts with a vowel, greet him



# user_name = input('Please enter your name: ')
# if user_name[0].lower() in ('a','e','i','o','u'):
#     print('Greeting to the person whose name starts with a VOWEL')


# Exercise (Easy)
# Ask the user for his name, and tell him if the last letter is a vowel or a consonant

# -------->    ANSWER  <-----------

# user_name = input('Please enter your name: ')
# if user_name[-1].lower() in ('a','e','i','o','u'):
#     print('Greeting to the person whose name ends with a VOWEL')
# else:
#     print('Your name ends with constant')    


# Exercise (Easy)
# Ask the user for two numbers (one after the other) and then print their sum

# -------->    ANSWER  <-----------

# user_input1 = input('Please enter a number ')
# user_input2 = input('Please enter a second number ')
# print(int(user_input1) + int(user_input2))

# Exercise (Medium)
# Challenge the user to print the longest sentence without any “A”, if he achieves it, tell him how many letters he wrote, else, print a fail message.

# -------->    ANSWER  <-----------

# user_sentence = input('please enter a sentence without using the Letter A:')
# if 'a' not in user_sentence:
#     print('good Job',len(user_sentence) - user_sentence.count(' '))
# else:
#     print( "You didn't pass the requirment")    




# Exercise (Medium)
# Ask the user for his full name (example: “John Doe”), and check the validity of his answer:

# The name should contain only letters.
# The name should contain only one space.
# The first letter of each name should be upper cased.

# -------->    ANSWER  <-----------

# user_full_name = input('Please enter your full name: ')
# first_letter =user_full_name.split(' ')

# if  user_full_name.isalpha():
#     print(' Name should only contain charcters ')
# elif user_full_name.count(' ') > 1:
#     print(' please re-enter your name ')
# elif first_letter[0][0].isupper() or first_letter[1][0].isupper():  
#     print('First letter should be capital ')  



# Exercise (Medium)
# Ask the user for a sentence, and then tell him how many words are in it.



# user_sentence = input('Please write a sentence : ')
# print(len(user_sentence.split(' ')))

# Exercise (Medium)
# Write a python program to get a string made of the first 2 and the last 2 chars from a given string, if the string length is less than 2, return instead the empty string.
# For example: "Helloworld" output "Held", while "Sik" returns ""

# -------->    ANSWER  <-----------

# user_sentence = input('Please write a sentence : ')
# new_string= user_sentence[:2]+ user_sentence[-2:]

# if len(user_sentence) < 3:
#     print(' ')
# else:
#     print (len(user_sentence))    

 
# Exercise (Medium)
# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) and then tell him how old he turnt/will turn this year.

# # -------->    ANSWER  <-----------
# import datetime
# date_entry = input('Enter a date in YYYY/MM/DD format : ')
# year, month, day = map(int, date_entry.split('-'))
# date1 = datetime.date(year, month, day)
# today=datetime.date.today()
# print(today.year-date1.year)

# Exercise (Hard)
# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) and then tell him how old he is today.

# -------->    ANSWER  <-----------

# import datetime

# date_entry = input('Enter a date in YYYY/MM/DD format : ')
# year, month, day = map(int, date_entry.split('-'))
# date1 = datetime.date(year, month, day)
# today=datetime.date.today()
# print(today.year-date1.year)


# For Loops

# Exercise (Easy)
# Write a program that counts the number of element for a list, without the len function.

# -------->    ANSWER  <-----------
# name=['Alex','Mike','Dylan','Yossi']
# count =0

# for elem in name:
#     count +=1
#     print(count)
    

# Exercise (Easy)
# Write a program that print every name that starts by ‘a’


# -------->    ANSWER  <-----------
# name=['Alex','Mike','Dylan','yossi','Alan']

# for elem in name:
#     if elem[0]=='A':
#         print(elem)


# Exercise (Easy)
# Write a Python program that prints all the numbers from 0 to 10 except 3 and 6.

# -------->    ANSWER  <-----------

# for i in range(1, 11):
#     if i == (3) or i==(6): 
#         pass;
#     else:
#         print (i)    

# Exercise (Easy)
# You have a list of users, and you want to remove every user that is below 16 years old.

# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.

# At the end, print the final list.

# Example list:
# -------->    ANSWER  <-----------
# names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']

# for i in names:
#     age = int(input(' please enter your age: '))
#     if age < 16 : 
#         names.remove(i)
#         print(names)
# Exercise (Easy)
# Use a for loop to print the numbers from 1 to 20, inclusive.

# -------->    ANSWER  <-----------
# start = 1
# stop  = 20
# step  = 1
# stop +=step #now stop is 6

# for i in range(start, stop, step):
#         print(i, end=', ')
# Exercise (Easy)
# Make a list of the numbers from one to one million, and then use a for loop to print the numbers.

# (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)

# # -------->    ANSWER  <-----------
# list=[]
# for i in range(1,100):
#     list.append(i)
#     print (list)

# Exercise (Easy)
# Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million.
#  Also, use the sum() function to see how quickly Python can add a million numbers .

# -------->    ANSWER  <-----------
# list=[]
# for i in range(1,1000001):
#     list.append(i)
# print (min(list))    
# print (sum(list))    
# print (max(list))    

# Exercise (Easy)
# Write a little program that concatenate two lists together without using the + sign.

# -------->    ANSWER  <-----------
# list1=[1,2,3]
# list2=[4,5,6]

# list1.extend(list2)
# print(list1)

# Exercise (Medium)
# Create a board as following by using for loops:

#     X
#     XX
#     XXX
#     XXXX
#     XXXXX
#     XXXXXX
#     XXXXX
#     XXXX
#     XXX
#     XX
#     X

# -------->    ANSWER  <-----------
# def pyramid():
#     list = []
#     for i in range (1,10):
#         list.append('*')
#         print(list)
#         if i == 9:
#             for i in range (2,10):
#                 list.remove('*')
#                 print(list)

# pyramid()        

# Exercise (Medium)
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

# -------->    ANSWER  <-----------
# list=[]
# for i in range (1,31):
#     if i%3 ==0:
#         list.append(i)
#         print(list)

# Exercise (Medium)
# Write a program that insert an item at a defined index.
# -------->    ANSWER  <-----------
# def insert_at_index():
#     user_item=int(input('please specifiy the item you want to add: '))
#     user_index=int(input('please specifiy where to add the item : '))
#     list=['Hello','world','blah','blah!!!!','!!!blah']
#     list.insert(user_index,user_item)
#     print(list)
# insert_at_index()    

# Exercise (Medium)
# Here is a list of popular car manufacturers: https://pastebin.com/bkBRuvAZ
# Paste it into your code, and store it in a variable.
# Convert it into a list using Python (don’t do it by hand!)
# Print out a message saying how many manufacturers/companies are in the list
# Print the list of manufacturers in reverse/descending order (Z-A)
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them
# Print the above information out with meaningful output messages.
# (Bonus: There are a few duplicates in the list:
# Remove these programmatically. (Hint: you can use sets to help you)
# Print out the companies without duplicates, in a comma-separated list with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), and also print out a message saying how many companies are now in the list).
# (Bonus: print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name)

# Exercise (Medium)
# You have two lists, current_players and new_players, use a while loop to transfer every player from new_players to current_players.
# -------->    ANSWER  <-----------
# current_players = ['Mario', 'Luigi', 'Peach']
# new_players = ['Blue Toad', 'Red Toad', 'Green Toad']
# # At the end of your program, print(current_players) should be:

# # ['Mario', 'Luigi', 'Peach', 'Blue Toad', 'Red Toad', 'Green Toad']

# for x in new_players:
#   current_players.append(x)
#   print(current_players)




# Exercise (Medium)
# Draw the following pattern using for loops:

#     *
#    **
#   ***
#  ****
# *****


# Exercise (Medium)

# What is the output of the following?¶
#     x = ['ab', 'cd']
#     for i in x:
#         i.upper()
#     print(x)
# -------->    ANSWER  <-----------
# same array
# Exercise (Medium)

# What is the output of the following?¶

# x = ['ab', 'cd']
# for i in x:
#     x.append(i.upper())
# print(x)
# -------->    ANSWER  <-----
# ------
# ['ab', 'cd','AB','CD']
# Exercise (Hard)
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.


# Exercise (Easy)
# Draw the following pattern using for loops:

# *
# **
# ***
# ****
# *****

# -------->    ANSWER  <-----------
# def pyramid():
#     list = []
#     for i in range (1,10):
#         list.append('*')
#         print(list)
# pyramid()        
       
# Exercise (Hard)
# Draw the following pattern using for loops:

# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *


# -------->    ANSWER  <-----------
# def pyramid():
#     list = []
#     for i in range (1,5):
#         list.append('*')
#         print(list)
#         if i == 4:
#             print(list)
#             for i in range (0,3):
#                 list[i]=('  ')
#                 print(list)
# pyramid()       
# 
#          
# Exercise (Hard)
# Draw the following pattern using for loops:

#       *
#      ***
#     *****

# Exercise (Hard)
# Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

# my_list = [2, 24, 12, 354, 233]
# for i in range(len(my_list) - 1):
#     minimum = i
#     for j in range( i + 1, len(my_list)):
#         if my_list[j] < my_list[minimum]:
#             minimum = j
#             if(minimum != i):
#                 my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
# print(my_list)

# -------->    ANSWER  <-----------
# [2, 12, 24, 233, 354]

# Exercise (Hard)
# Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

# my_list = [2, 13, 34, 23, 12, 111]
# for fillslot in range(len(arr)-1,0,-1):
#     max_pos = 0
#     for location in range(1, fillslot+1):
#         if arr[location] > arr[max_pos]:
#             max_pos = location
#     tmp = arr[fillslot]
#     arr[fillslot] = arr[max_pos]
#     arr[max_pos] = tmp
# Exercise (Hard)
# Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

# my_str = "I do"
# my_text = "What I can't build, I do not understand."
# found   = False
# index = 0
# for letter in my_text:
#     if letter == my_str[index]:
#         index += 1
#         if index == len(my_str):
#             found = True
#             break
#     else:
#         index = 0

# if found:
#     print("<{}> was found in the text !".format(my_str))
# else:
#     print("<{}> is not in the text".format(my_str))

# -------->    ANSWER  <-----------
# the index will increase to 3  when the function find the 'I"
# therefor it will run inside the if condition and it will be true so found will be trure and the function will break/stop so the result printed will be ""I do found in the text ""

# Exercise (Hard)
# Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

# Exercise (Hard)
# Write a program that put each word of a string in a list without using the split function.

# Exercise (Hard)
# Write a program that prints the longest word in a list.


# ---------> !!!!ANSWER !!!!! <--------------------------

# list=['theBiggestTest','biggerTest','test','hakunnaaMattatta']
# longest_word =''
# for i in list:
#    if len(longest_word) < len(i):
#        longest_word = i
#        print(longest_word)


# While Loops
# Exercise (Easy)
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value. As they enter each topping, print a message saying you’ll add that topping to their pizza .

# ---------> !!!!ANSWER !!!!! <--------------------------
 
# keep_adding = True

# while keep_adding:
#     user_item= input('please specifiy the item you want to add: ')
#     print('added to the pizza')
#     if user_item == 'quit':
#         print('Quitting')
#         break
   
   
    

# Exercise (Easy)
# A movie theater charges different ticket prices depending on a person’s age . If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15 .

# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket .
# ---------> !!!!ANSWER !!!!! <--------------------------
# while True:
#     user_age = int(input('please enter age: '))
#     if user_age < 3 :
#         print('ticket is free')
        
#     elif  12 > user_age > 3 :
#         print('ticket is 10$')
#     elif  user_age >= 12 :
#         print('ticket is 15$')

# Exercise (Easy)
# Given a list, use a while loop to print out every elements from the end to the beginning.
# answer
# wordList = ['hi', 'hello', 'this', 'that', 'is', 'of']
# i = len(wordList) -1
# while i >= 0:
#     print(wordList[i])
#     i -=1

# Exercise (Easy)
# Without your computer, guess the output of this piece of code:

# i = 1
# while True:    
#     if i == 3: 
#         break
#     print(i) 
#     i + = 1
# answer
# print 1
# print 2
# Exercise (Easy)
# Use a while loop to print every number from 5 to 100

# answer
# # i = 5
# while i < 100:
#     print(i)
#     i +=1 

# Exercise (Easy)
# What is the purpose of this program:

# user_input = input("> ")
# while user_input != "p4ssw0rd":
#     print("Access denied.")
#     user_input = input("> ")
# print("Access granted!")
# answer
# to ask for user password and to check if it matach the criteria 
# Exercise (Easy)
# What is the problem in this program:

# user_input = input("Password: ")
# while user_input != "my_password":
#     print("Access denied")
# print("Access granted")
# answer
# proplem if the user enter a wrong password the system will keep printing access denid 
# And how can you fix it ?
# we should add a break or re-ask for password
# Exercise (Medium)
# Take the last exercise, and apply it to a family, ask every member of the family their age, and at the end of the loop, tell them the cost of the tickets for the whole family.
total = 0
while True:
    user_age = int(input('please enter age: '))
    if user_age < 3 :
        print('ticket is free')
        
    elif  12 > user_age > 3 :
        print('ticket is 10$')
        total += 10
    elif  user_age >= 12 :
        print('ticket is 15$')
        total += 15
        print('total amount is : ' ,total,)
        break
# Exercise (Medium)
# Given a list, use a while loop to print out every element which his index is even.

# Exercise (Medium)
# A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.

# Write a program that ask every user their age, and then tell them which can see the movie.

# Try to add the allowed ones to a list.

# Exercise (Medium)
# This time you have a list of users, and you want to remove every user that is below 16 years old.

# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.

# At the end, print the final list.

# Exercise (Medium)
# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.

# Exercise (Medium)
# Count the number of spaces in a string.

# Exercise (Medium)
# Count the number of words in a string.

# Exercise (Medium)
# Write a program that calculate the number of upper case letters and lower case letters in a string.

# Exercise (Medium)
# Without your computer, guess the output of this program:

# index = 0
# my_list = [321, 312, 123, 434, 1235]
# while index < len(my_list):
#     s = str(my_list[index])
#     print(s[-1])
#     index += 1

# Exercise (Medium)
# What is the output of the following?¶

#     x = "abcdef"
#     i = "a"
#     while i in x:
#         x = x[:-1]
#         print(i, end = " ")
# Exercise (Medium)
# You have two lists, current_players and new_players, use a while loop to transfer every player from new_players to current_players.

# current_players = ['Mario', 'Luigi', 'Peach']
# new_players = ['Blue Toad', 'Red Toad', 'Green Toad']
# At the end of your program, print(current_players) should be:

# ['Mario', 'Luigi', 'Peach', 'Blue Toad', 'Red Toad', 'Green Toad']
# Exercise (Hard)
# Convert a string into password format
# Example:
# input : "mypassword"
# output: "***********"

# Exercise (Hard)
# Make a list called sandwich_orders and fill it with the names of various sandwiches .

# Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.

# As each sandwich is made, move it to the list of finished sandwiches.

# After all the sandwiches have been made, print a message listing each sandwich that was made.

# Exercise (Hard)
# Using the list sandwich_orders from Exercise 8, make sure the sandwich ‘pastrami’ appears in the list at least three times.

# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.

# Make sure no pastrami sandwiches end up in finished_sandwiches.

# Exercise (Hard)
# Encrypt and decrypt a string with Caesar cipher.

# Check on internet to understand how Caesar cipher works.

# Exercise (Hard)
# Create a python mastermind, make a program that asks the user for a string, and then generate a sequence of random letters (the length of the sequence should be the same as the user’s string) until he falls on the user’s string. At each iteration, the program can compare his random string to the user’s string, and keep the right letters.





















# Dictionnaries
# Exercise (Easy)
# Create a dict with your friends ages

# Exercise (Easy)
# Transform this dict:

# {0: 10, 1: 20}
# into this:

# {0: 10, 1: 20, 2: 30}
# Exercise (Easy)
# Write a Python program to get the maximum and minimum value in a dictionary.

# Exercise (Easy)
# Print every key and value of this dictionary using for loop, and then using while loop:

# products = {
# ‘SMART WATCH’: 550,
# ‘PHONE’ : 1000,
# ‘PLAYSTATION’: 500,
# ‘LAPTOP’ : 1550,
# ‘MUSIC PLAYER’ : 600,
# ‘TABLET’ : 400
# }
# Exercise (Medium)
# Write a Python program to remove duplicates values from Dictionary.

# Exercise (Medium)
# Write a Python script to check if a given key already exists in a dictionary.

# Exercise (Medium)
# Write a Python script to concatenate following dictionaries to create a new one.

# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Exercise (Medium)
# Use python to convert those two lists:

# list1 = ['Rick', 'Donald', 'Mickey' , 'Mario']
# list2 = ['Sanchez', 'Duck', 'Mouse', 'Kart']
# into this dictionnary:

# {
#     'Rick': 'Sanchez'
#     'Donald': 'Duck'
#     'Mickey': 'Mouse'
#     'Mario': 'Kart'
# }

# Exercise (Medium)
# Ask the user how many money he got, then display products that he can afford.

# products = {
# ‘SMART WATCH’: 550,
# ‘PHONE’ : 1000,
# ‘PLAYSTATION’: 500,
# ‘LAPTOP’ : 1550,
# ‘MUSIC PLAYER’ : 600,
# ‘TABLET’ : 400

# }
# Exercise (Medium)
# Get a number from the user, and then spell each number in words, for example, if the user input 1234:

# one two three four
# Exercise (Medium)
# Get a number from the user and create a dictionnary where the keys are every number from 1 to this number, and values are the square of keys.
# For example, if user input 5:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Exercise (Medium)
# step 1
# Make a dictionnary called contacts and add three of your friends with their phone number

# Example:

# {"Eyal":"0586878399",
# "John":"0542815674",
# "Mario":"0512345678"}
# step 2
# Add another person

# step 3
# Write a loop that print every contact with his number

# step 4
# Write a code that searches if a given name exists in the contacts

# step 5
# Write a code that searches if a given number exists in the contacts, if it exist, then print his name.

# step 6
# Given another dictionnary of contacts, add it to your dictionnary

# step 7
# Count how many contacts are in your dictionnary

# step 8
# Print the contacts in alphabetic order with their number

# Exercise (Hard)
# Write a Python program to combine two dictionary adding values for common keys. Go to the editor

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Output:

# {'a': 400, 'b': 400, 'd': 400, 'c': 300}














# Functions
# Exercise (Easy)
# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.

# Call the function, and make sure the message displays correctly.

# Exercise (Easy)
# Write a function called favorite_book() that accepts one parameter, title.

# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.

# Call the function, making sure to include a book title as an argument in the function call.

# Exercise (Easy)
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.

# The function should print a sentence summarizing the size of the shirt and the message printed on it.

# Call the function once using positional arguments to make a shirt.

# Call the function a second time using keyword arguments.

# Exercise (Easy)
# Make a list of magician’s names.

# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

# Exercise (Easy)
# Start with a copy of your program from Ex 6.

# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.

# Call show_magicians() to see that the list has actually been modified.

# Exercise (Medium)
# Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

# Create a function ‘get_age’.

# It should have three integer parameters: year, month, and day.
# Hard-code the current year and month in your code (there are better ways of doing this, but for now this will suffice.)
# After calculating the age, the function should return the age as an integer.

# Create a function ‘can_retire’.

# It should take 2 arguments: sex and date_of_birth.
# It should call your get_age function (with what arguments?) and receive an age back.
# Now it has all the information it needs in order to determine if the person with the given sex and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.

# Ask for the user’s sex as “m” or “f”.

# Ask for the user’s date of birth in the form “yyyy/mm/dd”, eg. “1993/09/21”.

# Call can_retire to get a definite value for whether the person can or can’t retire.

# Display a message to the user informing them whether they can retire or not.

# As always, test your code to ensure it works.

# Exercise (Medium)
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.

# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# Exercise (Medium)
# Write a function called describe_city() that accepts the name of a city and its country.

# The function should print a simple sentence, such as “Reykjavik is in Iceland”.

# Give the parameter for the country a default value.

# Call your function for three different cities, at least one of which is not in the default country.

# Exercise (Medium)
# Start with your work from Ex7.

# Call the function make_great() with a copy of the list of magicians’ names.

# Because the original list will be unchanged, return the new list and store it in a separate list.

# Call show_magicians() with each list to show that you have one list of the original names and one list with "the Great" added to each magician’s name.

# Exercise (Medium)
# Write a function called get_full_name() that receives three arguments: a first_name, a middle_name and a last_name. But the middle_name should be optional, if it’s omitted by the user, the name returned will only contain the first and the last name.

# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee. But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

# Exercise (Medium)
# Write a function that receives a list of numbers and return the highest number in the list and its position.

# Don’t use any built in function.

# Exercise (Medium)
# Write a function that receive a string in argument and returns if all the characters are uppercase or not.

# Exercise (Hard)
# Write a function that implements ceasar cypher, it receives a string and a number n as argument, and then shifts all the letters of the string by n places, and returns the encrypted string.

# Exercise (Hard)
# Write a function that takes a list of strings an prints them, one per line, in a rectangular frame.
# For example the list [“Hello”, “World”, “in”, “reallylongword”, “a”, “frame”] will result as:

# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************
# Exercise (Hard)
# Execute that code manually (without using your computer) and find the output.
# What is the purpose of it ?

# def insertion_sort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1

#      alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)
# Exercise (Hard)
# Write a function that converts English text to Morse code and another one that does the opposite.

# Check on internet for translation table, every letter is separated with a space and every word is separated with a slash /.













# Lists
# #### Exercise (easy)
# Create a list of your favorite colors.
# Add one color.
# Change the first color to ‘cyan’.

# Exercise (Easy)
# Create two lists, one of your favorite sweet food, and one of your favorite salty food.
# Then print which one is the longest.

# Exercise (Easy)
# Without using your computer, guess the output of:

# list1 = ['physics', 'chemistry', 1997, 2000]

# list2 = [1, 2, 3, 4, 5, 6, 7 ]

# print("list1[0]: ", list1[0])       #statement 1 
# print("list1[0]: ", list1[-2])      #statement 2 
# print("list1[-2]: ", list1[1:])     #statement 3 
# print("list2[1:5]: ", list2[1:5])   #statement 4 
# Exercise (Easy)
# Create a list containing the following sequences. Don’t hard-code the sequences.
# ​ a. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

# ​ b. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

# ​ c. -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4.

# ​ d. 10, 9, 8, 7, 6, 5.

# ​ e. 1, 3, 5, 7, 9, 11, 13.

# ​ f. (Bonus: 2, 4, 8, 16, 32, 64, 128)

# ​ g. (Is this possible? 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)

# Exercise (Easy)
# Recap – What is a float? What is the difference between an integer and a float?
# Earlier, we tried to create a sequence of floats. Did it work?
# Can you think of another way of generating a sequence of floats?
# Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.
# Exercise (Medium)
# Given this list:
# [825, 262, 627, 826, 285, 221, 730, 340, 750, 989, 272, 842, 383, 575, 810]
# Use the python built in list methods to print:

# The number of elements in the list
# The minimum element in the list
# The maximum element in the list
# The sum of all the numbers in the list
# Exercise (Medium)
# Take this list: ['spring', 'autumn', 'summer'].
# Add winter at the end of the list.
# Swap autumn and summer.

# Exercise (Medium)
# We are given a list of 10 integers to analyze. Repeat the questions below with the following lists of numbers:

# [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
# [44, 9l, 8, 24, -6, 0, 56, 8, 100, 2]
# [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
# [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# Store the list of numbers in a variable.

# We will now print some information about the list of numbers. Each time, print the answer together with a helpful message that tells the user what you are printing.

# Print the following information:

# a. The list of numbers – printed in a single line

# b. The list of numbers – sorted in descending order (largest to smallest)

# c. The sum of all the numbers

# A list containing the first and the last numbers only

# (Bonus: The average of all the numbers)

# (Bonus: The largest number)

# (Bonus: The smallest number)

# Exercise (Medium)
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it into your code, and store it as a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…)
# How many sentences it contains
# How many words it contains
# How many unique words it contains
# (Bonus: How many non-whitespace characters it contains)
# (Bonus: The average amount of words per sentence in the paragraph)
# (Bonus: the amount of non-unique words in the paragraph)
# Exercise (Hard)
# Reminder:
# A list element can be any data type, thus it can also be a list. For example, a list of lists, where each sub list contains a name and an age:

# my_family = [['John', 14], ['Micheal', 18], ['Dorit', 20]]
# Create a list of your 3 favorites actors, this list should be a list of lists, each sub list is in this format: [actor_name, reason_you_like_him].
# Use this list to print something like this:

# My favourite actors are:
# Homer Simpsons, because he is so funny.
# Johnny Depp, because he acts so good.
# Me, because it's me.
# Exercise (Hard)
# Ask the user to give you the four seasons, separated by a space.
# Use python strings methods to put each word in a list. And then check if this list has really 4 seasons.












# Sets
# Exercise 1 (Easy)
# Create a set called my_fav_numbers with your favorites numbers.

# Add two new numbers to it.

# Remove the last one.

# Create a set called friend_fav_numbers with your friend’s favorites numbers.

# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.

# Exercise 2 (Easy)
# Do the same with a tuple.

# Exercise 3 (Medium)
# You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score