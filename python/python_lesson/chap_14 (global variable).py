#CHAP_14- GLOBAL AND LOCAL VARIABLE :

l=10                        ### global variable : any function in the program can use this variable by defaultly

def function(n):
    l=5                     ### local variable : only that function can use this variable
    m=8
    print(l,m)
    print(n,"i have printed")

function("this is me")
#print(m)              ### error will occur, because m is local variable and you cannot use that out of the function


#GOBAL KEYWORD:       to change global variable value for that function
k=12
def function2():
    global k         ### can change the value of global variable
    k=k+45           ### without this you can not change value of global variable
    print(k)

function2()


def harsh():
    x=20                                ### this is not a global variable,its inside the function
    def rohan():
        global x
        x=88                            ### thats why this x cannot be changed 
    print("brfore calling rohan()",x)
    rohan()
    print("after calling rohan()",x)
harsh()
print(x)

#                              """END"""
