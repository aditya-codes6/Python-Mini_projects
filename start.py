# # # # # # # # # # # # print("Hello World")
# # # # # # # # # # # # x = 1
# # # # # # # # # # # # if x == 1:
# # # # # # # # # # # #      # indented four spaces
# # # # # # # # # # # #     print("x is 1.")

# # # # # # # # # # # # import pyjokes
# # # # # # # # # # # # print(pyjokes.get_joke())


# # # # # # # # # # # import pyttsx3
# # # # # # # # # # # pyttsx3.speak("This application is made by thee greatest developer in history the great Aditya ")


# # # # # # # # # # a = 5 
# # # # # # # # # # b = 7 
# # # # # # # # # # c = a + b 
# # # # # # # # # # print(c)


# # # # # # # # # a =int(input("Enter the number :"))
# # # # # # # # # b = int(input("Enter the second number :"))
# # # # # # # # # c = (a + b)/2
# # # # # # # # # print(c) 

# # # # # # # # a = int(input("Enter the side of a square :"))
# # # # # # # # print("The area of a square is \t",a*a)




# # # # # # # # name = "Aadi"
# # # # # # # # print(name[0:3])
# # # # # # # # print(name[-3:-1])


# # # # # # # r = '''I stopped asking why you changed,
# # # # # # # and started noticing how.
# # # # # # # The words that once felt endless,
# # # # # # # feel distant somehow now.

# # # # # # # I still remember little things,
# # # # # # # the jokes, the late-night talks,
# # # # # # # how a simple “hey” from you
# # # # # # # could brighten up my thoughts.

# # # # # # # Maybe we were meant to meet,
# # # # # # # but not meant to stay.
# # # # # # # Some people become memories
# # # # # # # before they walk away.

# # # # # # # And if someday you think of me,
# # # # # # # I hope you smile, not cry—
# # # # # # # because for a little while,
# # # # # # # you made my ordinary life feel alive.'''
# # # # # # # print(r)


# # # # # # # a = "My name is aadi ansd iam a bad bad bad bad boy with bad intentions"
# # # # # # # print(a.replace("bad","good"))


# # # # # # a = "Aaditya is a boy"
# # # # # # print(a.startswith("red"))


# # # # # name = input("What is your name ?")
# # # # # print(f"Good afternoon sir/madam {name}" )


# # # # name = "Aaditya is a \"human\" "
# # # # print(name)

# # name = "Aadtiya is a good boy with  good intentions  and he is great"
# # print(name.find("i"))
# # print(name)
# # print(name.replace("  "," "))


# age = input("What is your age ?")
# print(f"This human is {age} old" )

#import pyttsx3
#pyttsx3.speak("My name is aditya and i hate a letter N")


b = int(input("Enter the total food spendings :"))
c = int(input("Enter the total travel spendings :"))
d = int(input("Enter the total other expenses "))
p = int(input("Enter the total person numbers :"))

total = b + c + d 
division = total / p

#PERSON 1 DATA 
p1_food = int(input("Enter the food expense of p1 : "))
p1_travel = int(input("Enter the travel expense of p1 : "))
p1_other = int(input("Enter the other expensesof p1 : "))
p1_total = p1_food  + p1_travel + p1_other

# PERSON 2 DATA 
p2_food = int(input("Enter the food expense of p2 : "))
p2_travel = int(input("Enter the travel expense of p2 : "))
p2_other = int(input("Enter the other expensesof p2 : "))
p2_total = p2_food  + p2_travel + p2_other


#PERSON 3 DATA
p3_food = int(input("Enter the food expense of p3 : "))
p3_travel = int(input("Enter the travel expense of p3 : "))
p3_other = int(input("Enter the other expensesof p3 : "))
p3_total = p3_food  + p3_travel + p3_other

final_p_total = p1_total + p2_total + p3_total

if total == final_p_total:
    print("There is no error or misunderstanding between amount distribution")
else :
    print("ERROR :-   There is an error occur , So kindly check your calculation properly ONCE AGIAIN")
