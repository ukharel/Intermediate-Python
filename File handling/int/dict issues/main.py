with open('samplea.txt','w') as f:
    f.write(5)
#  write only take str not int
#  to write num, you must change it into str

with open('samplea.txt','w') as f:
    f.write('5')


# It also does not take dict, it must be converted into str
d={
    'name':'ujjwal',
    'age':24,
    'status': 'single'
}

with open('samplea.txt','w') as f:
    f.write(str(d))


#  You can read the content of the dictionaries but cannot access its key and value, that means it is a great problem.
with open('File handling\int\dict issues\samplea.txt','r') as f:
    s=f.read()
    print(s)

