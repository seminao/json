import json
# d={'4': 5, '6': 7, '1': 3, '2': 4}
# s=sorted(d.keys())
# e={}
# for i in s:
#     for k in d:
#         if k==i:
#             e[i]=d[k]
# f=open("meraki4.json","w")
# y=json.dump(e,f,indent=2)
# f.close()

import json
d={'4': 5, '6': 7, '1': 3, '2': 4}
y=json.dumps(d,indent=2,sort_keys=True)
print(y)