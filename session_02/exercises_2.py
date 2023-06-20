# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
# width = 65
# height = 78
# area = width * height

# print("Rectangle of width " + str(width) + " and height " + str(height) + " has an area of " + str(area) + ".")

# # 2. Write code that prints the length of the string, 'python'.
# python = "Python"
# name_length = len(python)

# print(name_length)

# # 3. Print out the first and third letter of the word 'python'.
# print(python[0])
# print(python[2])

# # 4. Ask the user to enter their name, and print out `Hello, <name>`.
# name = input("What's your name? ")

# print ("Hello " + name)

# # 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
# age = int(input("How old are you? "))
# age_in_10_years = age + 10

# print("In 10 years you will be " + str(age_in_10_years))

# # 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
# #   In 15 years time you will be <age_in_15_years_time>`.
# print("Hello " + name + ". You are currently " + str(age) + " years old.")

# age_in_15_years = age + 15

# print("In 15 years time you will be " + str(age_in_15_years))


# # 7. Ask the user to enter their hometown, print it out in uppercase letters.

# hometown = input("What is your home town? ")

# print(hometown.upper())

# # 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
# colour = input("What is your favourite colour? ")

# print(len(colour))


# # 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
# weather = input("How's the weather today? ")
# month = input("What month is it? ")

# print(" ")

# print("It is " + month + " and the weather is " + weather + " today.")



# # 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
# #   `It is <month> and the average temperature is <average_temperature> degrees celsius`.

# t1 = int(input("Enter a temperature "))
# t2 = int(input("Enter a (different) temperature "))
# t3 = int(input("Enter a (different) temperature "))
# t4 = int(input("Enter a (different) temperature "))
# t5 = int(input("Enter a (different) temperature "))

# average =  ((t1 + t2 + t3 + t4 + t5) / 5)

# print(average)



# # 11. Print out the above sentence but make the month upper case.

# print("It is " + month.upper() + " and the weather is " + weather + " today.")

# # 12. Create a variable that holds your favourite animals and print it out. 
# #    Make sure the animals are all on different lines and tabbed.

# animals = ("\tPenguin\n\tGiraffe\n\tBadger")
# print(animals)

# # 13. Ask the user to enter their name as well as a number. 
# #    Print out the uppercase character at that position in the string.

# namenumber = input("Enter your name followed by a number ")

# print(namenumber[:1])

# # 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
# string = "WelcometoPython"

# print(string[0:15:2]) 

fullname = "Alan" + "Turing"
length = len(fullname)
middle_letter = fullname[int(length / 2)].lower()
print(middle_letter)