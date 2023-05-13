if __name__ == '__main__':
    N = int(input())
    mylist=[]

my_list = []
for x in range(N):
    partes = input().split()
    if "append" in partes:
        my_list.append(int(partes[1]))
    elif "insert" in partes:
        my_list.insert(int(partes[1]), int(partes[2]))
    elif "print" in partes:
        print(my_list)
    elif "remove" in partes:
        my_list.remove(int(partes[1]))
    elif "sort" in partes:
        my_list.sort()
    elif "reverse" in partes:
        my_list.reverse()
    elif "pop" in partes:
        my_list.pop()