a=10#global
def local():
    a=100#local scope
    print(a)
def en():
    a=200# enclosed scope
def closed_function():
  a=1#localsope
   print(a)
  closed-function()
  print(a)
print(a) 
en()
local()    
