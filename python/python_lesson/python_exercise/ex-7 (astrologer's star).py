#EX-7 : ASTROLOGER'S STAR

#PROBLEM : MAKE AN DIAGRAM AS BELOW WITH NUMBER OF ROWS and direction of diagram(x) INPUTED BY AN USER
#          IF x is 0 : ***
#                      **
#                      *
#          IF x IS 1 : *
#                      **
#                      ***

# SOLUTION :
n=int(input("enter number of rows\n"))
x=int(input("select 1 or 0 to flip the the diagram\n"))
n_of_row=1

if x==0:                    #false
    while n>0:
        print("*"*n)
        n=n-1
else:                       #true
    while n>0:
        print("*"*(n_of_row))
        n_of_row=n_of_row+1
        n=n-1

#OUTPUT :
"""
enter number of rows
10
select 1 or 0 to flip the the diagram
0
**********
********* 
********  
*******   
******    
*****     
****      
***       
**        
*   
"""

#                                    """END"""
