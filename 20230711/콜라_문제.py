def solution(a, b, n):
    answer = 0
    while (n >= a):
        left_bottle = n % a # 남은 병의 수
        n = (n//a)*b    # 교환 후 받은 콜라 수
        answer += n #받은 콜라 수 만큼 answer 갱신
        n += left_bottle  #남은 콜라 수 만큼 콜라 수 갱신
    return answer

a1 = 2
b1 = 1
n1 = 20
print("1번 : ",solution(a1, b1, n1))

a2 = 3
b2 = 1
n2 = 20
print("2번 : ",solution(a2, b2, n2))