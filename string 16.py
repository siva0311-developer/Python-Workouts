a="hello world "
b="this is a python"

#concadination (+)
c=a+b
print(c)

#append(+)
d=b+" this is string class"
print(d)

#repeat (*)

print(a*4)

#built-in function for strings

#upper
print(a.upper())

#len
print(len(a))

# lower
print(b.lower())

#capitalize

print(a.capitalize())

#ord()

a="A"
print(ord(a))

#id()
print(id(a))


#string slicing(cut) variable_name[start:end]

x=b[:]
print(x)
x=b[4:8]
print(x)
x=b[4:]
print(x)
x=b[:8]
print(x)


#string sride slicing(cut) variable_name[start:end:step]
a="amaran_ramsiva"
print(a[::4])
#we can use slicing method is list.
'''a[2]='a'
print(a)'''

#count(string:start:end)
a="hello world"
print(a.count("w"))

#chr()
a=100
print(chr(a))
