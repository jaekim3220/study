def solution(number, limit, power):
    divList = []  # 약수 list
    for i in range(1, number + 1):  # 1부터 number까지
        div = 0
        for j in range(1, int(i ** (1 / 2)) + 1):  # 1부터 i의 제곱근까지
            if i % j == 0:
                div += 1
            if div > limit:  # limit값을 초과하면 power
                div = power
        divList.append(div)
    return sum(divList)


print(solution(5, 3, 2))  # 10
print(solution(10, 3, 2)) # 21



