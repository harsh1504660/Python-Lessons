#CHAP_6- SETS :

from re import S

s=set()
print(type(s))      ### class set

s_from_list = set([1,2,3,4])
print(s_from_list)     ### set  (returns equal value)

s.add(1)           ### add element in set
s.add(15)
print(s)

union_set = s.union(s_from_list)               ### union of twq set
print(union_set)

s.remove(15)                   ### remove element from set
print(s)

#                            """END"""