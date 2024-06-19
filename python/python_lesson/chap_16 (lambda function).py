#CHAP_16- LAMBDA FUNCTION :       MORE SIMPLE THAN NORMAL FUNCTION

#lambda / anonymouse function:
def minus1(a,b):
    return a-b
print("subtraction by normal function",minus1(10,6))

minus = lambda x,y : x-y                                  ### this is lambda function, both ways are equal
print("subtraction by lambda function",minus(10,6)) 


# ANOTHER EXAMPLE
def a_first(a):
    return a[1]
a= [[1,14],[4,5],[5,7]]
a.sort(key=a_first)
print(a)
 
sort1 = lambda b : b[0]
a.sort(key=sort1)
print(a)

#                              """END"""