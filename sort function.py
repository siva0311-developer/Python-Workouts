
'''a=[10,9,8,30,50,70]
b=(10,20,30,40,50)
a[2]=45
print(a)
b[4]=60
print(b))
'''
'''b=a.copy()
print(a.sort(reverse=True))
print(a)
print(b)'''


#creating tuple using function:

#tuple()

a=tuple(x*2 for x in range(1,20,1))
print(a)

#changing element in tuples:

b=(10,20,30,40,50)
c=list(b)
print(c)
c[2]=43
c=tuple(c)
print(c)


#accessing single element in tuple

print(c[4])


d=b+c
print(b+c)

#unpacking tuple:

e=(80,90,70,60)
(f,g,h,i)=(80,90,70,60)
print(e,'\n',f,'\n',g,'\n',h,'\n',i,'\n')

# count(),index(),min() and max() in tuple

y=min(e)
print(y)
z=max(e)
print(z)
