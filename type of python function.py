#type of function:-
'''
1.user define function
2.recursive function
3.lambda function
4.bulit in function(type(),input(),count(),id()...)

#recursive function
def ram():
    print("heyy")
    s=int(input("Enter the s value:"))
    if s==1:
        ram()
    else:
      print("po")
ram()                            #this recursive function:-       


#lambda function:-
y=lambda a:a**2    #power value
print(y(6))

x=lambda a,b,c:a+b+c
print(x(1,2,3))

#Returning value from function
def add():
  a=int(input("Enter A Value:"))
  b=int(input("Enter B Value:"))
  e=int(input("Enter B Value:"))
  return(a,b,e)

c,d,f=add()
print(c+d+f)'''

a=100
def ram():
    a=10
    b=20
    print(a+b)
print(a)
ram()
          
