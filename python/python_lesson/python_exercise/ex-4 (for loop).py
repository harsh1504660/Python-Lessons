#EX-4 : FOR LOOP

#PROBLEM :  MAKE LSIT AND RETURN ONLY VALUES WHICH ARE NUMBERS AND GREATER THAN 6

#SOLUTION :
#from curses.ascii import isalnum


list1=[1,2,"harsh","jay hind",420,"saras",89,"gulab",7,10]

for item in list1:
    if str(item).isnumeric() and item >6:
        print(item)

#OUTPUT :
"""
420
89
7
10
"""

#                             """END"""