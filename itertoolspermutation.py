from itertools import permutations
str_a,n=input().split()
n=int(n)
permutationlist=list(permutations(str_a,n))
permutationstring=sorted(list(''.join(permutation) for permutation in permutationlist))
for x in permutationstring:
    print(x)