# writing number in file.

'''lst=[input('enter a number: '),input('enter second number: ')]
with open('sample3.txt','w') as f:
    for i in lst:
        f.write(f'{i}\n')
#  reading number from file
with open ('sample3.txt','r') as f:
    num1 = int(f.readline())
    num2= int(f.readline())

    num3=num1+num2
    print(num3)'''
    

user_input = input('Enter a number to make mutiplication of: ')

with open('sample2.txt' , 'w') as f:
    user_input_num = int(user_input)
    for j in range(1,user_input_num+1):
        for i in range(1,11):
            f.write(f'{j}*{i}={j*i}\n')

with open('sample2.txt','r') as f:
    content= f.read()
    print(content)