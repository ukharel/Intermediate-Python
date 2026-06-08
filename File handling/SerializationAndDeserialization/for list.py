# In order to read and write file as it, we use seralization and deserialization.
#  Serialization is the process of converting python data types in to JSON format
#  Deserialization is the process of converting JSON into python data type


import json

# To write for list
L = [1,2,3,4]
L1=['mango','apple','orange','litchi','banana','cheery']
with open('demolst.json','w') as f:
    json.dump(L1,f)

# To read the json file

with open('demolst.json','r') as f:
    print(json.load(f))


