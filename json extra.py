
# Convert the following Vehicle Object into JSON
# o/p:{"name": "Toyota Rav4","engine": "2.5L","price": 32000}

# import json
# Sort JSON keys in and write them into a file
# Sort following JSON data alphabetical order of keys

# sj= {"id" : 1, "name" : "value2", "age" : 29}
# o/p:{"age": 29,"id": 1,"name": "value2"}

# Convert the following Vehicle Object into JSON
# import json

# class Vehicle:
#     def _init_(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price

# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
# s=a[:-22]
# s1=a[4:-18]
# s2=a[8:-14]
# s3=a[12:-10]
# print(s)
# abcd
# efgh

# a="abcdefghijklmnopqrstuvwxyz"
# i=0
# while i<len(a):
#     print(a[i],end="")
#     if i>1 and i%4==0:
#         print()
#     i=i+1




a="abcdefghijklmnopqrstuvwxyz"
i=0
f=4
while i<len(a):
    j=i
    while j<=f:
        print(a[i])
        j=j+1
    i=i+4
    f=f+4
    
