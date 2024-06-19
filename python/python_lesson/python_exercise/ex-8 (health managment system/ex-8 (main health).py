#EX-8 : HEALTH MANAGMENT SYSTEM

#PROBMLEM : MAKE HEALTH MANAGMENT SYSTEM FOR 3 PERSON TO SHOW AND EDIT THIER INTAKE EXCERSIZE SCHEDULD

#SOLUTION :

def getdate():
    import datetime
    return datetime.datetime.now()
v=str(getdate())


def edit():
    person=input("select person\npress 1 for harsh\npress 2 for saras\npress 3 for mrunmay\n")
    if person=="1":
        choice=input("what do want to edit\npress 1 for diet\npress 2 for excersize\n")
        if choice=="1":
            f=open("harsh_diet.txt","a")
            data=input("add harsh's diet:\n")
            f.write("["+ str(v)+"]"+""+ data+"\n")
            print("information added succesfully!")
            f.close()
        else:
            f1=open("harsh_ex.txt","a")
            data1=input("add harsh's excersize:\n")
            f1.write("["+str(v)+"}"+data1+"\n")
            print("information added succesfully!")
            f1.close()
    elif person=="2":
        choice1=input("what do want to edit\npress 1 for diet\npress 2 for excersize\n")
        if choice1=="1":
            f2=open("saras_diet.txt","a")
            data3=input("add saras's diet:\n")
            f2.write("["+str(v)+"]"+""+data3+"\n")
            print("information added succesfully!")
            f2.close()
        else:
            f3=open("saras_ex.txt","a")
            data3=input("add saras's excersize:\n")
            f3.write("["+str(v)+"]"+""+data3+"\n")
            print("information added succesfully!")
            f3.close()
    else:
        choice2=input("what do want to edit\npress 1 for diet\npress 2 for excersize\n")
        if choice2=="1":
            f4=open("mrunmay_diet.txt","a")
            data4=input("add mrunmay's diet:\n")
            f4.write("["+str(v)+"]"+""+data4+"\n")
            print("information added succesfully!")
            f4.close()
        else:
            f5=open("mrunmay_ex.txt","a")
            data5=input("add mrunmay's excersize:\n")
            f5.write("["+str(v)+"]"+""+data5+"\n")
            print("information added succesfully!")
            f5.close()

def retrive():
    person1=input("select person\npress 1 for harsh\npress 2 for saras\npress 3 for mrunmay\n")
    if person1=="1":
        choice3=input("press 1 for diet\npress 2 for excersize\n")
        if choice3=="1":
            f5=open("harsh_diet.txt")
            r1=f5.read()
            print("harsh's diet:\n"+r1)
            f5.close()
        else:
            f6=open("harsh_ex.txt")
            r2=f6.read()
            print("harsh's excersize:\n"+r2)
            f6.close()
    elif person1=="2":
        choice4=input("press 1 for diet\npress 2 for excersize\n")
        if choice4=="1":
            f7=open("saras_diet.txt")
            r3=f7.read()
            print("saras's diet:\n"+r3)
            f7.close()
        else:
            f8=open("saras_ex.txt")
            r4=f8.read()
            print("saras's excersize:\n"+r4)
            f8.close()
    else:
        choice5=input("press 1 for diet\npress 2 for excersize\n")
        if choice5=="1":
            f9=open("mrunmay_diet.txt")
            r5=f9.read()
            print("mrunmay's diet"+r5)
            f9.close()
        else:
            f10=open("mrunmay_ex.txt")
            r6=f10.read()
            print("mrunmay's excersize"+r6)
            f10.close()


action=input("select the action:\npress 1 for editing\npress 2 for retriving\n")
if action=="1":
    edit()
else:
    retrive()

#OUTPUT:
"""
select the action:   
press 1 for editing  
press 2 for retriving
2
select person      
press 1 for harsh  
press 2 for saras  
press 3 for mrunmay
1
press 1 for diet     
press 2 for excersize
1
harsh's diet:
[2022-10-12 00:09:46.419525]chicekn tikka
[2022-10-12 00:32:11.044276]dal chawal
[2022-10-12 00:32:28.422513]onion kofta curry
[2022-10-12 00:32:48.085471]lemon rice with apple juice
"""




    




    
   
