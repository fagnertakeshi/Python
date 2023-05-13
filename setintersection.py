n1=int(input())
studfrench=set(map(int, input().split()))
n2=int(input())
studenglish=set(map(int, input().split()))

print(len(studfrench.union(studenglish)))