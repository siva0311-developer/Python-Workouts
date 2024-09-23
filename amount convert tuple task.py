a=['raj','amaran','siva','ram','dev']
b=[100,2000,450,555,790]
b=list(b)
sender=input("Enter The SenderName:")
Receiver=input("Enter The ReceiverName:")
EnterAmount=int(input("Enter The Amount"))

for i in a:
    if(i==sender):
        print("Sender Name Is Available")
        d=(a.index(i))
        e=b[d]-EnterAmount
        b[d]=e
        print("Sender Bal Amt",e)
    elif(i==Receiver):
         print("Receiver Name Is Available")
         s=(a.index(i))
         f=b[s]+EnterAmount
         b[s]=f
         print("Receiver Credit Amt",f)
       
    

b=tuple(b)
print(b)


























