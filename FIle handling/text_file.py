
#  writing content in the file. 'w' rewrites the content again everytime
# f = open('sample.txt','w')
#  # the open keyword open the or make the file and put it into the RAM for work.
# f.write('This is the file demo') 
# # write function let you write content on the file.
# f.close() 
# # It is necessary to close the file to freeup the resources used by RAM and put it into the harddisk.


#  Reading content from the file. 'r' helps to read the whole content of the file
# f= open('sample.txt','r')
# content= f.read()
# print(content)
# f.close()

# Appending content to the file.'a' helps to add the content if you don't want to erase totally.

'''f = open('sample.txt','a')
f.write('This is the append text')
f.close()'''

# Using with keyword, with act as a context manager in the python that ensures the file get closed properly after it finishes executing the code.
#  it also take multiple file at once

# with open('sample.txt','w') as f:
#     f.write('This is the end.')
#     f.write('\nThis is the beginning.')
#     f.write('\nThis is the goal.')

# Readline

# with open('sample.txt','r') as f:
#     content= f.readline()
#     print(content,end='')

# readlines, it return the list as output

# with open('sample1.txt','r') as f:
#     content = f.readlines()
#     print(content)

# writelines, it writes the content from the list.

# lst = ['hello','\nHow are you?','\nHow you been?','\nAre you interested in AI? ']
# with open('sample1.txt', 'w') as f:
#     f.writelines(lst)

# using seek function- it helps to point whereever you want to go in the file
# with open('sample1.txt','r') as f:
#     f.seek(5)
#     content =f.read(15)
#     print(content)


    # writing content using seek function 
# with open('sample.txt','w') as f:
#     f.seek(5)
#     f.write('hey jude')
#     f.seek(0)
#     f.write('go behind')
