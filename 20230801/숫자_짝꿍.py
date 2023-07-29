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

print(solution("100", "2345"))  # -1
print(solution("100", "203045"))    # 0
print(solution("100", "123450"))    # 10
print(solution("12321", "42531"))   # 321
print(solution("5525", "1255")) # 552