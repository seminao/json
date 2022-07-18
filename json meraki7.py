#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29

# {
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of      navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }
# import json
# u=int(input("enter the number"))
# e={}
# i=0
# while i<u:
#     k=input("enter the keys")
#     v=input("enter the values")
#     e[k]=v
#     i=i+1
# f=open("meraki7.json","w")
# json.dump(e,f,indent=3)
# f.close()

import json
a={}
filename="meraki7.file"
with open("meraki7.file") as f:
    for i in f:
        key,value=i.strip().split(None,1)
        a[key]=value
print(json.dumps(a,indent=4))
file=open("meraki7.json","w")
json.dump(a,file,indent=4)
file.close()
# f.close()



