def solution(number, limit, power):
    answer = 0
    divList = []    #약수 리스트
    for i in range(1,number+1):    #약수를 구할 숫자 확인
        div = 0 #약수 개수 초기화
        for j in range(1, i+1):
            if i % j == 0:  #기사에게 할당된 숫자 i를 1~i까지 나눌 때 나머지가 0이면 약수
                div += 1
        if div > limit: #공격력이 limit보다 높으면
            div = power #power로 대체
        divList.append(div)
    answer = sum(divList)
    return answer

# n = 5
# l = 3
# p = 2
# print(solution(n, l, p))

n = 10
l = 3
p = 2
print(solution(n, l, p))