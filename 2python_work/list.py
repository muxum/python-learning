me = ['lazy','noisy']
print(me[0].title())
#change something now
me[0]= 'a'
print(me[0])
#addddddd
me.append('h')
print(me[-1])
# insert(,) make other memebers go  to the right
print('\n') 
print(me)
me.insert(1,'anyway')
print(me)
#delet something ,other type in same way
del me[0]
del me[-1]
#point!!!! 4 to 3 !!! pay attttentionnnn to the new set //go to Left
print(me)
lastone = me.pop()   #amazing
print(lastone)
print(me)
me=['a','b','c','d','e']
so = me.pop(2)
print(so)
#add something in the ( ) ,oprate anything you want


"""trying a new way, play print()"""
'''??  green? great'''
print(so + str(me) + "\nSDA")
print(so + me + "\nSDA")
