#CHAP_17- EXTERNAL AND BUILT IN MODULE :  use documentation for functions of modules

#random
from logging import exception
from pickle import EXT4
import random

random_number = random.randint(0,4)         ### gives random number between the specified range
print(random_number)

rand = random.random() * 100               ### f=gives random number between range, can be fractional value
print(rand)


lst=["star plus","dd1","aaj tak","code with harry"]
choice=random.choice(lst)                    ### randomly selects value from list
print(choice)

#math
import math
a=math.factorial(5)                        ###gives factorial
print(a)

b=math.isqrt(47)
print(b)                                     ### gives integer sqrt

c=math.remainder(10,5)
print(c)                                    ### gives reminder of any devesion

d=math.log10(25)                            ### gives vaue of log to the base 10
print(d)

e=math.radians(30)                          ### converts degree to radian
print(e)

f=math.sin(0.5)                             ### gives sine of radian
print(f)

#webbrowser
import webbrowser
webbrowser.open_new("www.wikipedia.com")        ### opens the url in broser

webbrowser.open_new_tab("mygov.com")            ### opens new tab

#                                   """END"""
