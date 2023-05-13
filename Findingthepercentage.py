if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    soma = 0
    for valor in student_marks[query_name]:
        soma += valor

    media = soma / len(student_marks[query_name])

    print("{:.2f}".format(media))