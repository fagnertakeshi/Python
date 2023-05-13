n=int(input())

words_count={}

for _ in range(n):
    word=input()
    if word not in words_count:
        words_count[word]=1
    else:
        words_count[word]+=1

print(len(words_count.values()))       

print(*words_count.values())