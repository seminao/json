# # write code to print the value of key2
# # O/p:value2
# import json
# j= """{"key1": "value1", "key2": "value2"}"""
# y=json.loads(j)
# print(y["key2"])

# **Ex5: Access the nested key ‘salary’ from the following JSON
# o/p:7000
import json
j= """{ "company":{ "employee":{ "name":"emma","payable":{ "salary":7000,"bonus":800}}}}"""
y=json.loads(j)
print(y["company"]["employee"]["payable"]["salary"])

