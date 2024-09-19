list=[10,20,30,40,30,50,60,70,30,40,50]
x=int(input("enter the duplicate value"))
y=[]
for i in list:
      if(i==x):
       y.append(i)
       print(x)
