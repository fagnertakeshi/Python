if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_sorted_list = sorted(list(arr))
    print(my_sorted_list[my_sorted_list.index(max(my_sorted_list))-1])