#CHAP 19 : ARGS & KWARGS 

def funargs(*args):
    for item in args:
        print(item)

har = ["harsh","joshi","subodh"]        ### you can add n numbers of items in list without adding more arguments every time 
                                        ### args= should be written as *args
                                        ### kwargs= should be written as **kwargs 
funargs(*har)

#                                       END




