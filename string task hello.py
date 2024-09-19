string=input("Enter The String")
task=len(string)
for i in range(task):
    for j in range(i+1):
     print(string[j],end=" ")
    print()


