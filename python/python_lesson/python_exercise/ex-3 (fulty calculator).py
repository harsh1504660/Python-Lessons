#EX-3 : FAULTY CLCULATOR

#PROBLEM : DESIGN A CALCULATOR WHICH WILL CORRECTLY SOLVE ALL THE PROBLEMS EXCEPT THE FOLLOWING
#           45*3=555, 56+9=77 , 56/6=4
#          YOUR PROGRAM SHOULD TAKE OPERATOR AND THE TWO NUMBERS AS INPUT FROM THE USER AND THEN RETURN THE RESULT

#SOLUTION :
n1=int(input("enter the first nuumber\n"))
n2=int(input("enter the second number\n"))
print("press + for addition\npress - for subtraction\npress * for multiplication\npress / for dividation")
opr=input("select the operator from above\n")

if opr=='+':
    if n1==56 and n2==9:
        print('result: 77')
    else:
        print("result: ",n1+n2)
elif opr=='-':
    print("result :",n1-n2)
elif opr=='*':
    if n1==45 and n2==3:
        print('result :555')
    else:
        print("result :",n1*n2)
elif opr=='/':
    if n1==56 and n2==6:
        print("result :4")
    else:
        print("result",n1/n2)
else:
    print("select a valid operator") 
print("thank you for using the calculator!!")

#OUTPUT:
"""
enter the first nuumber
45
enter the second number
3
press + for addition
press - for subtraction       
press * for multiplication    
press / for dividation        
select the operator from above
*
result :555
thank you for using the calculator!!
"""

#                         """END"""