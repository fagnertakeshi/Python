students=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
students.sort(key=lambda x: (x[1], x[0]))
second_lowest_score = sorted(set([x[1] for x in students]))[1]
second_lowest_names = [x[0] for x in students if x[1] == second_lowest_score]
for name in second_lowest_names:
    print(name)