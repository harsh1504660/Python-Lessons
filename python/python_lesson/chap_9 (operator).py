#CHAP_9- OPERATORS IN PYTHON :

"""
ARITHMATIC OPERATOR
ASSIGNMENT OPERATOR
COMPARISON OPERATOR
LOGICAL OPERATOR
IDENTICAL OPERATOR
MEMBERSHIP OPERATOR
BITWISE OPERATOR
""" 

#ARITHMATIC OPERATOR :
print("ARITHMATIC OPERATOR")
print("5+6 is",5+6)
print("5-6 is",5-6)
print("5*6 is",5*6)
print("5/6 is",5/6)
print("5//6 is",5//6)
print("5**6 is",5**6)
print("5%6 is",5%6)

#ASSIGNMENT OPERATOR :
print("ASSIGNMENT OPERATOR")
x=5
print(x)
x+=7                        ### adds seven in the x
print(x)
x/=7                        ### MINUS SEVEN FROM X
x-=7

#COMPARISION OPERATOR :
print("COMPARISON OPERATOR")
i=5
print(i==5)
print(i>5)
print(i<5)
print(i>=5)
print(i<=5)

#LOGICAL OPERATOR :
print("LOGICAL OPERATOR")
a= True
b= False
print(a and a)               ### output:true
print(a or b)                ### output:true
print(a or a)                ### output:true
print(a and b)               ### output:false

#IDENTICAL OPERATOR :
print("IDENTICAL OPERATOR")
a= True
b= False
print(a is b)                ### output:false
print(a is not b)            ### output:true

#MEMBERSHIP OPERATOR :
print("MEMBERSHIP OPERATOR")
list=[2,3,2,5,3,935,6]
print(32 in list)            ### output:false
print(32 not in list)        ### output:true
print(2 in list)             ### output:true

#BITWISE OPERATOR :
print("BITWISE OPERATOR")
"""
0-00
1-01
2-10
3-11               IN BINARY
"""
print(0 & 1)                 ### output:0    [and function]
print(0 | 1)                 ### output:1    [or function]

#                        """ END """
