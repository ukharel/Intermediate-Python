# Pickle is the concept that when object is converted into byte data and unpickling in back into object so that it can be run into different platfrom.

import pickle
class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender= gender

    def show_detail(self):
        return f'{self.name} is my name and I am {self.gender}'

    
p=Person('ujjwal','male')
with open('pickle.pkl','wb') as f:
    pickle.dump(p,f)

with open('pickle.pkl','rb') as f:
    pickle.load(f)

print(p.show_detail())