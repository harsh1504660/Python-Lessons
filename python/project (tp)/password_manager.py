print("WELCOME TO PASSWORD MANAGER")
app_password="harsh123"
inp_password=input("enter password\n")
chance=0

while inp_password != app_password :
    inp_password=input("password incorrect enter again\n")
    chance=chance+1
    if chance==2:
        print("you enterd incorrect password 3 times try again after some time!!!")
        exit()

def find():
    print("")
    user_name=input("enter username of password:\n")
    f=open(user_name+".txt")
    view=f.read()
    print(view)
    f.close()

def edit():
    print("")
    opr=input("press 1 for make new password\npress 2 for edit existing password\n")
    if opr==1:
        print("")
        new_user=input("enter user name or website:\n")
        new_password=input("enter passwrod:\n")
        f1=open(new_user+".txt",'w+')
        f1.write("user name: "+new_user+"\n")
        f1.write("password: "+new_password)
        f1.close()
        print("password updated sccesfuly!!")
    else:
        print("")
        existing_user=input("enter user name or website name:\n")
        change_passwrd=input("enter new password:\n") 
        f2=open(existing_user+".txt",'w+')
        f2.write("user name: "+existing_user+"\n"+"password: "+change_passwrd)
        f2.close()
        print("password updated succesfuly!!")

print("")
rtry='y'
while rtry=='y':       
    opr=str(input("press 1 for finding the password\npress 2 for editing the password\n"))
    if opr=="1":
        find()
    else:
        edit()
    print("")    
    rtry=input("do you want to use it again?\npress y for reuse\npress n for exit\n")
    if rtry=='n':
        print("Thanks for using PASSWORD MANAGER!!")



#OUTPUT
"""
WELCOME TO PASSWORD MANAGER
enter password
harsh123

press 1 for finding the password
press 2 for editing the password
2

press 1 for make new password
press 2 for edit existing password
1

enter user name or website name:
mobile unlock
enter new password:
1504
password updated succesfuly!!
"""

#                                         END
