import json
dict1 ={"emp1": {"name": "Lisa","designation": "programmer","age": "34","salary": "54000" },
    "emp2": {"name": "Elis","designation": "Trainee","age": "24","salary": "40000"},}
out_file = open("myfile.json", "w") 
json.dump(dict1, out_file, indent = 6)
out_file.close()

# import json
# a={9: "John","age": 30,"city": "New York"}
# f=open("my file.json","w")
# json.dump(a,f,indent=4)
# f.close()

# import json
# dict={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }
# f= open("file.json", "w") 
# json.dump(dict,f, indent = 6) 
# out_file.close()


# import json
# # d='{"4": 5, "6": 7, "1": 3, "2": 4}'
# f=open("meraki4.json","r")
# y=json.load(f)
# print(y)