from itertools import combinations_with_replacement

word,n=input().split()
n=int(n)
word=sorted(word)
comb=list(combinations_with_replacement(word,n))

for s in comb:
    print(''.join(s))