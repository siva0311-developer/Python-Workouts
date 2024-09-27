d={'name':'siva','age':20,'city':'madurai'}
for i in d.keys():
    print(i)         # to output keyvalues


d={'name':'siva','age':20,'city':'madurai'}
for i in d.values():
    print(i)          # to output values 
      
d={'name':'siva','age':20,'city':'madurai'}
for i in d.items():   # to output values & keyvalues
    print(i)

for i in d.items():
    x,y=i
    print(x,":",y)

 # to copy function
 
e=d.copy()
print(e)


#get()

k=d.get('age')
print(k)


# set default

x=d.setdefault('major','b.comca')
print(d)

#fromkeys()

x=("address","state")
y="tamilnadu"
z=d.fromkeys(x,y)
print(z)


#add to input
o={}
m=input("Enter The Key")
n=input("Enter The Values")
for i in o.items():
    print(i)
for i in o.setdefault (m,n):
 print(o)
    
