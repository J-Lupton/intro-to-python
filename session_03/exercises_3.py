# # Session 3 Exercises

# ## Section A
# # 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
# name = input("What is your name? ")

# if name == "Bob":
#   print("Welcome Bob!")


# # 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
# name = input("What is your name? ")

# if name != "Alice":
#   print("You're not Alice!")

# # 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
# #   If they get it wrong, print "Password failure".

# password = input("Enter password: ")

# if password == "qwerty123":
#   print("You have successfully logged in.")

# if password != "qwerty123":
#   print("Password incorrect.")

# # 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#   print("Even")
# else:
#   print("Odd")

# # 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"

# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))

# num_result = num1 + num2

# if num_result >=21:
#   print("Bust")

# if num_result <=21:
#   print("Safe")

# # 6. Ask the user to enter the length and width of a shape and check if it is a square or not.

# width = int(input("Enter a number:"))
# length = int(input("Enter a number:"))

# if width == length:
#   print("Is square")
# else:
#   print("Is rectangle")

# # 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
# #   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

# salary = int(input("Enter your salary: "))
# years_of_serv = int(input("Enter your years of service: "))
# bonus = int(salary * 0.1)

# if years_of_serv > 3:
#   print("Your salary is " + str(salary) + " and your bonus is " + str(bonus))
# else:
#   print("Your salary is " + str(salary) + " and you have no bonus")



# # 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.

# number = int(input("Enter a number:"))


# if number >= 0:
#   print(number ** 3)
# else:
#   print(number / 2)

  



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".

# name = input("What is your name? ")

# if name == "Alice":
#   print("Hello Alice")
# elif name == "Bob":
#   print("You're not Bob! I'm Bob.")
# else:
#   print("You must be Charlie?")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

# age = int(input("What is your age? "))

# if age < 11:
#   print("You're too young to go to this school")
# elif age < 16:
#   print("You can come to this school")
# elif age == 0:
#   print("You're not born yet")
# else:
#   print("You're too old for this school")


# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".

# month = input("What month is it? ")

# if month == "May" or month == "April" or month == "March":
#   print(month + " is in Spring.")
# elif month == "January" or month == "December" or month == "February":
#   print(month + " is in Winter.")
# elif month == "June" or month == "July" or month == "August":
#   print(month + " is in Summer.")
# elif month == "September" or month == "October" or month == "November":
#   print(month + " is in Autumn.")
# else:
#   print("I don't know.")
  
# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

# num1 = int(input("What is number 1? "))
# num2 = int(input("What is number 2? "))

# if num1 % 2 == 0 and num2 % 2 == 0:
#   print("Even")
# elif num1 % 2 != 0 and num2 % 2 != 0:
#   print("Odd")
# else:
#   print(num1 * num2)

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.

# num1 = int(input("What is number 1? "))
# num2 = int(input("What is number 2? "))

# if num1 > num2:
#   print(num1)
# else:
#   print(num2)
  

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

# salary = int(input("Enter your salary: "))
# years_of_serv = int(input("Enter your years of service: "))
# bonus20 = int(salary * 0.2)
# bonus15 = int(salary * 0.15)
# bonus10 = int(salary * 0.1)

# if years_of_serv > 7:
#   print("Your salary is " + str(salary) + " and your bonus is " + str(bonus20))
# elif years_of_serv > 5:
#   print("Your salary is " + str(salary) + " and your bonus is " + str(bonus15))
# elif years_of_serv > 3:
#   print("Your salary is " + str(salary) + " and your bonus is " + str(bonus10))
# else:
#   print("Your salary is " + str(salary) + " and you have no bonus")

# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.

# name1 = input("What is person 1's name? ")
# age1 = int(input("What is person 1's age? "))
# name2 = input("What is person 2's name? ")
# age2 = int(input("What is person 2's age? "))
# name3 = input("What is person 3's name? ")
# age3 = int(input("What is person 3's age? "))

# if age1 > age2 and age1 > age3:
#   print(name1)
# elif age2 > age1 and age2 > age3:
#   print(name2)
# elif age3 > age1 and age3 > age2:
#   print(name3)
# else:
#   print("All ages are the same")
  
# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
  ##   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

age = 0

if age == 0: 
    print("You aren't born yet") 
elif age <= 13:
    print("You are 13 or younger") 
elif age < 18: 
    print("You are between 14 and 17") 
else: 
    print("You are 19 or over")