#CHAP_12- FILE IO BASICS :

"""
"r" - open file for reading....DEAFULT
"w" - open a file for writing
"x" - creats a file if not exist
"a" - add more contetnt to a file
"t" - text mode
"b" - binary mode
"+" - read and write
"""

# FILE READING :
#f = open("demo_1.txt")
#content = f.read()                ### opening the file [reading]
#print(content)
#f.close()
 
#print(f.readline())               ### only for one line
#print(f.readlines())              ### read as list


#FILE WRITING:
#f = open("demo_2.txt","w")                ### write a content in file and delete the previous content
#f.write("harsh bhai bahut acche hai\n")
#f.close()

#f=open("demo_2.txt","a")                  ### add content to file [append]
#f.write("harsh bhai gande hai")

#FILE READ AND WRITE:
#HANDEL READ AND WRITE BOTH
f=open("demo_2.txt","r+")
print(f.read())
f.write("\nthank you")

#                            """END"""