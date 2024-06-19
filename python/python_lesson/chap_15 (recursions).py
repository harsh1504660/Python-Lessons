#CHAP_15- RECURSIONS :  USE FUNCTION IN ANOTHER FUNCTION

def fibonachi(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)

number = int(input("enter a number"))
print(fibonachi(number))




# no more data


"""0 1 1 2 3 5 8 13 
1 2 3 4 5 6 7 8 """