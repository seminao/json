import json
# a=["neelam","programer","24","2400"],
# ["komal","trainer","24","20000"],
# ["anuradha","HR","25","40000"],
# ["Abhishek","manager","29","63000"]
# b=["name","designation","age","salary"]
# o/p
# a={"emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#         },"emp2":
#         { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         },"emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000"}}


import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"] 
e=["name","destination","age","salary"]
dic1={}
dic2={}
dic3={}
dic4={}
dic={}
i=0
while i<len(a):
    dic1[e[i]]=a[i]
    dic2[e[i]]=b[i]
    dic3[e[i]]=c[i]
    dic4[e[i]]=d[i]
    i=i+1
dic["emp1"]=dic1
dic["emp2"]=dic2
dic["emp3"]=dic3
dic["emp4"]=dic4
print(dic)
f=open("meraki8.json","w")
j=json.dump(dic,f,indent=4)
f.close()

# d={}
# i=0
# while i<len(a):
#   s={}
#   m="emp"+str(i+1)
#   j=0
#   while j<len(a[i]):
#     s[b[j]]=a[i][j]
#     j=j+1
#   i=i+1
#   d[m]=s
# with open("meraki 8.json","w") as f:
#   y=json.dump(d,f,indent=1)


# import json
# a=[["neelam","programer","24","2400"],
# ["komal","trainer","24","20000"],
# ["anuradha","HR","25","40000"],
# ["Abhishek","manager","29","63000"]]
# b=["name","designation","age","salary"]
# s={}
# i=0
# while i<len(a):
#     t={}
#     # e={}
#     j=0
#     while j<len(a[i]):
#         s[b[j]]=a[i][j]
#         j+=1
#     i+=1
#     m="emp"+str(i)
#     t[m]=s
#     print(t)
    
    