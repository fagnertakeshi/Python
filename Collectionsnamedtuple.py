from collections import namedtuple
n=int(input())
columns=[item for item in input().split(' ') if item!= '']
marks_index = columns.index('MARKS')
values=[]

for _ in range(n):
    values.append([item for item in input().split(' ') if item!= ''])

sum=0;

for i in range(n):
    sum=sum+ int(values[i][marks_index])
    
print(sum/n)
