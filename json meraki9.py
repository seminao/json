
import json
list={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":
    "30","ice_cream":"20",}}
item=input("enter the item:")
quantity=int(input("how much you want to buy:"))
a=list["shopping_list"][item]
r=int(a)-quantity
list["shopping_list"][item]=r
f=open("meraki9.json","w")
y=json.dump(list,f,indent=2)

                                          
