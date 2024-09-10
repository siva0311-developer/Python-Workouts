'''TASK SENDER'''

a=['raj','amaran','siva','ram','dev']
b=[100,2000,450,555,790]                   
sender=input("Enter The SenderName:")
Receiver=input("Enter The ReceiverName:")
EnterAmount=int(input("Enter The Amount"))
for i in a:
    if i==sender and i==receiver:
        print("Sender Name Is Available")
    
    else:
         print("Sender Name Is  Not Available")

