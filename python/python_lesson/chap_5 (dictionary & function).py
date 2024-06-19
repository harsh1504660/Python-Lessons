#CHAP_5-DICTIONARY AND ITS FUNCTIONS :

"""DICTIONARY IS KEY VALUE PAIRS"""
from this import d


d1={}
print(type(d1))  

d2 = {"harsh" : "joshi","tanmay":"dhamnae","bhushan":"khillare","rushikesh":{"f":"sunil","s":"khairnar"}}
#print(type(d2))        ### dictionary 
print(d2)

print(d2["rushikesh"]["f"])  
 
d2["shravan"]="ahire"                 ### add element in dictionary
print(d2)

del d2["shravan"]
print(d2)                             ### delet element from dictionay

print(d2.get("harsh"))                ### gives value of element 

d2.update({"vedant":"ufade"})         ### add element in dictionary
print(d2)

print(d2.keys())                      ### shows key
print(d2.items())                     ### shows items
 
#                           """END"""