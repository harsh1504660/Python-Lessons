#CHAP_11- TRY EXCEPTION HANDLING :       (used for resolving the error)

from logging import exception


print("enter first number")
num1=(input())
print("enter second number")
num2=(input())

try:
    print("addition of the values is",int(num1)+int(num2))     ### if error occurs in this line
except Exception as e:                                       ### this line will print that error and continue to run,
                                                                   # the remaining program
    print(e)


print("this line of code is very important")                            ### remaining program wont stop

#                                    """END"""
