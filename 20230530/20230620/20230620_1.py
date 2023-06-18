'''
동전을 오름차순으로 정렬
만들 수 있는 최솟값을 1부터 시작해 순차적으로 증가
동전을 하나씩 선택하면서 만들 수 있는 금액 갱신
동전을 모두 사용한 후에도 만들 수 없는 금액을 찾으면 그 값을 반환
'''

def money(prices):
    prices.sort()
    minimum = 1 # 만들 수 없는 최솟값의 초기 값
    for a in prices:
        
        if a <= minimum:
            # print(minimum)
            minimum += a
            

    return minimum
prices1 = [3, 2, 1, 1, 9]
print(money(prices1))

prices2 = [1, 3, 5, 7]
print(money(prices2))