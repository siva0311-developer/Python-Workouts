'''a={'key':'values'}#normal dictionary



a={'key':{'key':'values'}} # Nested Dictionary'''

a={'a1':{'name':'siva','age':21,'city':'madurai'},
   'a2':{'name':'sivaram','age':22,'city':'manamadurai'},
   'a3':{'name':'sivaraj','age':23,'city':'mamadurai'},
   }
b=a['a1']
print(b)
b=a['a2']
print(b)
b=a['a3']
print(b)

#accessing values in dictionary

for i in(a.keys()):
      print(i)
      for j in b.keys():
        print(j,'\t:',a[i][j])
     
      
      
  


'''print(a['a1']['name'])'''

