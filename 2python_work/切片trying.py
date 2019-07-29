l=['a','b','c','d','e','f']
print(l[1:2])
print(l[:2])
print(l[2:])
print(l[:])
print(l[-3])###means print No.3 ((counting from the last)
###-1 is the bN0.1;;; -2 is the bNo.2;;;-3 is the bNo.3;;
### -3 to END  we have
print(l[-3:])
###let's try from the head
print(l[:-3])

la = l#only connet l & la, l& la piont to one list ,but there list:la is not EXISTed.
#means,la is  another l type.
#no,you can't->also can give  "la" the l's CUT  ! ! !  
print("\n" + str(la))
l.append('gg')
print(la)

del l[-1]

la =l[:]
l.append('nn')
print(la)
##############################################
print("the first 3 items in the list l")
print(l[:3])
print("3 items from the middle of the list are")

print(l[(len(l)//2)-1:(len(l)//2)+2])#####looooooKK
print("the last 3 in list l")
print(l[-3:])
