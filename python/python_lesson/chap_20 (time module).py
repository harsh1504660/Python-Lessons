#CHAP 20 : TIME MODULE

import time         

initial = time.time()                              ### for knowing the execution time of the program

k=0
while k>45:
    print("my name is harsh joshi")
    k=k+1
print("while loop ran in",time.time()-initial,'seconds')   ### this is the time take by comp to run while loop

initial2=time.time()
for i in range(45):
    print("my name is harsh joshi")
print("for loop ran in",time.time()-initial2,'seconds')     ### this is the time take by comp to run for loop



localtime = time.asctime(time.localtime(time.time()))       ### gives the local time
                                                            ### asctime = converts the local time from touple to std 
print(localtime)

#                                     END
