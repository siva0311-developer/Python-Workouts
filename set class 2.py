'''a={}
print(type(a))
b=set({})
print(type(b))
c=set({10,20,40})
c.add(30)
print(c)
      
e=[50,60,70]
c.update(e)
print(c)'''

g={10,20,30,40,50}
f={50,60,70,80,40,10}
'''print(g.union(f))                  #add two values
print(g.intersection(f))            #take common value
print(g.difference(f))              #difference between g 
print(g.symmetric_difference(f)) #difference between g and f
del g                               #del output is error
print(g) '''   
'''f.remove(80)           # remove particular value
print(f)
f.clear()                 #clear all value
print(f)
g.pop()                    #del last value
print(g)'''
g.discard(30)
print(g)    
