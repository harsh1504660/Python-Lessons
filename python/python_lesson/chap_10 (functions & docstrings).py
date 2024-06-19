#CHAP_10- FUNCTION AND DOCSTRINGS :

def function1():                            ### defining function
    print("hello your are in function")
function1()                                 ### executing function

def function2(a,b):                            
    print("hello your are in function",a+b)
function2(4,5)                              ### adding 4 and 5

def function3(c,d):
    average=(c+d)/2
    return average                          ### helps to stor the value in veriabe
v=function3(4,7)
print(v)                              ### giving the verage of c adn d


#DOCSTRING : (reules of the function)
def function3(c,d):
    """this function will calcuate the average"""               ### docstring
    average=(c+d)/2 
    return average                          
print(function3.__doc__)                                ### printing the docstring

#                              """END"""