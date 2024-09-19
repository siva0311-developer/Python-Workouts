a=['raj','amaran','siva','ram','dev']
b=[100,2000,450,555,790]
j=0
sender=input("Enter The SenderName:")
Receiver=input("Enter The ReceiverName:")
EnterAmount=int(input("Enter The Amount"))

for i in a:
    if(i==sender):
        print("Sender Name Is Available")
        print("Sender Bal Amt",b[j]-EnterAmount)

    elif(i==Receiver):
     print("Receiver Name Is Available")
   
     print("Receiver Credit Amt",b[j]+EnterAmount)
       
    j+=1




























