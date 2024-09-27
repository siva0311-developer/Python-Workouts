#example for function

'''def print2():
    a="SIVARAM"
    print(a)
print2()
print("this is python function")
print2()
print2()
print2()
print2()
print2()'''


def calculator():
    a=int(input("Enter 1st Value:"))
    b=int(input("Enter 2nd Value:"))
    c=input("\n1.add\n2.sub\n3.multi\n4.div\n5.modulo\n\n\t\t\choose anyone~")

    def add():
        print(a+b)
    def sub():
        print(a-b)
    def multi():
        print(a*b)
    def div():
        print(a/b)
    def m_div():
        print(a%b)

    if c=='+':
        add()
    
    elif c=='-':
        sub()
    
    elif c=='*':
        multi()
    
    elif c=='/':
        div()
    
    elif c=='%':
        m_div()
    else:
     print("not valid")
calculator()
