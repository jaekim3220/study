def solution(X, Y):
    answer = ''
    for num in range(10):
        count_x = X.count(str(num))
        count_y = Y.count(str(num))
        count_min = min(count_x, count_y)
        if count_min > 0:
            answer += str(num) * count_min

    if not answer:
        answer = "-1"
    else:
        answer = ''.join(sorted(answer, reverse=True))

    return answer

X = "100"
Y = "2345"
print(solution(X, Y))

X = "100"
Y = "203045"
print(solution(X, Y))

X = "100"
Y = "123450"
print(solution(X, Y))

X = "12321"
Y = "42531"
print(solution(X, Y))

X = "5525"
Y = "1255"
print(solution(X, Y))