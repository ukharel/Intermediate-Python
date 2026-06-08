import json
d={
    'name':'somebody',
    'address':'Nepal',
    'age':34
}

with open('demodict.json','w') as f:
    json.dump(d,f,indent=4)

with open('demodict.json','r') as f:
    d=json.load(f)
    print(d)
    print(type(d))
    print(d['name'])
