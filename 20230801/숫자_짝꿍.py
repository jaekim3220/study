def solution(X, Y):
    answer = ''
    sameNum = ''
    for i in range(len(X)):
        if X[i] in Y:
            sameNum += X[i]
    sameNum = sorted(sameNum, reverse=True)
    if len(sameNum) == 0:
        answer = "-1"
    else:
        answer = ''.join(sameNum)
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