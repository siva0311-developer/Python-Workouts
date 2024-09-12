'''TASK SENDER'''

a=['raj','amaran','siva','ram','dev']
b=[100,2000,450,555,790]                   
sender=input("Enter The SenderName:")
Receiver=input("Enter The ReceiverName:")
EnterAmount=int(input("Enter The Amount"))

for i in a:
 
 if(i==sender):
    print("Sender Name Is Available")
    d=(a.index(i))
    print(" Sender Bal Amt",b[d]-EnterAmount)
 elif(i==Receiver):
     print("Receiver Name Is Available")
     p=(a.index(i))
     print("Receiver Credit Amt",b[p]+EnterAmount)










    
''' print(i)'''

   
  


'''if i==sender:

     print("Sender Name Is Available")
    
    else:
         print("Sender Name Is  Not Available")'''

