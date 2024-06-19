#CHAP_4-LIST AND ITS FUNCTION : 

from re import A


greocery=["harpic","deodrent","bhindi","chocolate","vim bar"]
print(greocery[1])

numbers=[5,3,6,41,2,]
print(numbers[2])
#numbers.sort()         # sort the list in ascending order
print(numbers)

#numbers.reverse()
print(numbers)          # reverse the list

print(numbers[0:3])     # slicing 
print(numbers[0:5:2])   # excended slicing

#FUNCTIONS OF LIST :
print(max(numbers))     # same for minimum

numbers.append(10)      # add element to the end of list 
print(numbers)

numbers.insert(1,67)    # insert element at any index [ here 1 is index no. and 67 is inserted number]
print(numbers)

numbers.remove(2)       # removes a number 
print(numbers)

numbers.pop()           # remove the last element 
print(numbers)

numbers[1]=8            # can change the number 
print(numbers)

"""
list= is imutable (can change)
touple = is immutable (cannot change)
"""

tp=(1,2,3)              # this is touple
#tp[1] = 8
#print(tp)
#error = beacause touple's value cannot be changed

a=1
b=8
"""temp = a
a = b
b = temp
print(a,b)"""             # swapping

#OR

a,b=b,a
print(a,b)

#                         """END"""