#CHAP_8- FOR LOOPS & WHILE LOOP:

list1=["harsh","saras","mrunmay","aboli"]

for item in list1:
    print(item)

#WHILE LOOP :
i=0
while i<45:
    print(i+1,end=" ")
    i=i+1

while True:
    print(i+1,end=" ")
    if 1==44:
        break                  ### stop the loop
    i=i+1

while True:
    if i+1<5:
        continue                ### continiues the upper loop till the the condition is true
    print(i+1,end=" ")
    if 1==44:
        break                 
    i=i+1

#                             """END"""