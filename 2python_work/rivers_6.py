dec ={'a':'ant','c':'car','b':'blue','g':'ant','b':'boss','k':'knife'}#point:: no "=" inside
############              #################
##### new "b"  covered the old "b"  ...####
##### printed "boss"  but  no "blue"   ####
###########################################
print(dec)
for i in dec.keys() :
	print(i)
print('\n')

for i in dec.values() :
 print(i)
print("#################")
print("for i in sorted(set(dec.values()),reverse = True):")
for i in sorted(set(dec.values()),reverse = True):
	print(i)
print("\nfor i in set(sorted(dec.values(),reverse = True)):")
for i in set(sorted(dec.values(),reverse = True)):
	print(i)
print("\nfor i in set(sorted(dec,reverse = True)):")
for i in set(sorted(dec,reverse = True)):
	print(i)
print("\nfor i in sorted(set(dec),reverse = True):")
for i in sorted(set(dec),reverse = True):
	print(i)

dec["mimikkoUI"]='mengmengnaiaaaa'
print(dec)

import numpy as np
