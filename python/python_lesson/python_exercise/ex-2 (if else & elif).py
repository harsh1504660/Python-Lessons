#EX-1 : IF ELSE & ELIF

#PROBLEM : CREAT A DRIVING PERMISSION APP USING IF ELSE AND ELIF 

#SOLUTION :
age=int(input("enter your age\n"))

if age<7:
    print("enter a valid age")
    exit()
elif age>70:
    print("enter a valid age")
    exit()

if age>18:
    print("you can drive")
elif age<18:
    print("you can not drive")
else :
    print("we can not decide")
print("thank you for using the app!!")

#OUTPUT:
"""
enter your age
25
you can drive
thank you for using the app!!
"""

#                         """END"""