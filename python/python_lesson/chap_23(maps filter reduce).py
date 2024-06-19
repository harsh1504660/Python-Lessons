#CHAP_23 - MAP FILTER AND REDUCE :

#MAP :
numbers = ['1','2','35','44']

numbers=list(map(int, numbers))            ### apply any fuction to the all elements of list

def sqr(n):
    return n*n
num = [2,3,1,2,4,6,6,5,300,1]
square = list(map(sqr,num))                ### applies sqr function to num list 
print(square)

#FILTER :
list1 = [1,2,3,5,1,83,85]
def is_greater(num):
    return num>5

gr_than_5 =list(filter(is_greater,list1))       ### gives only number from list that are greater than 5
print(gr_than_5)

def even(num1):
    return (num1%2==0)
even_num = list(filter(even,list1))
print(even_num)

#REDUCE :
from functools import reduce 
list2 = [2,5,7,9,5,60]
def addi(x,y):
    return x+y
num = reduce(addi,list2)                          ### make any operation between the elements of list
print(num)

str1 = ['harsh','subodh','joshi']
def conc(word,word1):
    return word+word1
ad=reduce(conc,str1)
print(ad)

                                      #END
 