import json
class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender= gender

    
p=Person('ujjwal','male')

# for str data type
'''def show_obj(p): 
        if isinstance(p,Person):
            return (f'{p.name},{p.gender}')'''

# for dict data type
def show_obj(p):
        if isinstance(p,Person):
            return {'name':p.name,'gender':p.gender}


with open('democlass.json','w') as f:
    json.dump(p,f,default=show_obj,indent=4)


# to load file

with open('democlass.json','r') as f:
    d=json.load(f)
    print(d)
    print(type(d))
