#CHAP_13- MORE ON FILES :

#f = open("demo_1.txt")
#print(f.tell())                      ### to know where is file pointer
#print(f.readline())
#print(f.tell())
#print(f.readline())
#print(f.tell())

#f.seek(10)                           ### reset the file pointer
#f.close()

#OPEN FILE WITH BLOCK :
with open("demo_1.txt") as f:         ###  no need to close the file
    a=f.read(4)
    print(a)

#                                 """END"""
