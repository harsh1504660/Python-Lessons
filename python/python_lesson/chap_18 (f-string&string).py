#CHAP_18- F-STRING & STRING :

a1=3
me="harsh"
a="this is {} {}"                 ### replace bracket with pre defined variable
b=a.format(me,a1)
print(b)

#fstring
c=f"this is {me} {a1} {4*78}"     ### addition of string
print(c)                          ### replace '+' to add the string

import math
d=f"this is cos of 65 {math.cos(65)}"
print(d)

#                                  """END"""

