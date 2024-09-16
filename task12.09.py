list=[10,20,30,40,50]
'''z=0
x=int(input("enter the searching value"))
s=int(input("enter the deleting value"))
for i in list:
    if(i==x):
        z=1
if(x==list):
    print("value is available")
else:
    print("value is available")'''

'''list.remove(30)
print(list)'''

'''list=[10,20,30,40,50]
s=int(input("enter the deleting value"))
for i in list:
    if(i==s):
        continue
    print(i)'''
  
list=[10,20,30,40,50,60,70,80,50,20,30,40,50]
d=int(input("Enter The Duplicate Value"))
for i in list:
    if(i==d):
        list.remove(i-d)
        print(list)
        break
    
    
    
