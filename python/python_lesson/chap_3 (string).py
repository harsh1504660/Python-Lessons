#CHAP3-STRING DATATYPE:

mystr="harsh is a good boy"
print(mystr[2])
#output : r    ...........   index number of string, starts with 0

print(mystr[0:5])
#output :harsh  ..........  gives whole word between the indexes, 0 is including and  is excluding 

print(len(mystr))            # lenght of string

print(mystr[0:8:3])         # skips number of letters 
#output : hsi
 
print(mystr[-3:-2])
#output : b      .........  negative index : starts with right side of string 

print(mystr[::-1])
#output : yob doog a si hsrah    ....... reverses the string 

print(mystr[::-2])
#output : ybdo  ihrh     ........  firstly reverses the string then select letters with gap of 2 

###FUNCTION OF STRING : 
mystr1="harshisagoodboy" 
print(mystr1.isalnum())     # isalnum : checks whether string has spaces 

print(mystr.endswith("boy"))
#output : true          .......  endswith : checks whether string ends with boy 

print(mystr.count("o"))
#output : 3           ........ counts number of o's in the string 

print(mystr.capitalize())           # capitalizes the first the letter 
print(mystr.find("is"))             # find the index of required word

print(mystr.upper())
#output : HARSH IS A GOOD BOY

print(mystr.replace("is","are"))
#output : harsh are a good boy     ....... replaces the is with are
###find more string function

#                                   """END"""