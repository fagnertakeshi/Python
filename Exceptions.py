n=int(input())

for _ in range(n):
    try:
        a, b = [int(x) for x in input().split()]
        print(int(a/b))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
        continue
    except ValueError as e:
        print("Error Code:",e)
        continue