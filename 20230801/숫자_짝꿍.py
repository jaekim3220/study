def solution(X, Y):
    answer = ''
    for num in range(10):
        count_x = X.count(str(num)) # X의 숫자를 확인
        count_y = Y.count(str(num)) # Y의 숫자를 확인
        count_min = min(count_x, count_y)   # 공통 숫자를 찾는 만큼 짧은걸 선택한다
        if count_min > 0:   # 공통 숫자가 있는 경우
            answer += str(num) * count_min  # 공통 숫자를 결과 문자열에 추가합니다. (예: 5가 3번 등장하면 '555'를 추가)

    if not answer:  # 공통 숫자 없으면 -1 반환
        answer = "-1"
    else:
        answer = ''.join(sorted(answer, reverse=True))

    return answer

print(solution("100", "2345"))  # -1
print(solution("100", "203045"))    # 0
print(solution("100", "123450"))    # 10
print(solution("12321", "42531"))   # 321
print(solution("5525", "1255")) # 552