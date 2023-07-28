'''
로또의 최고 순위와 최저 순위
0이 아닌 숫자 중 일치하는 개수
0인 숫자 중 일치하는 경우의 수
맞춘 개수에 따른 순위 추출
'''

def solution(lottos, win_nums):
    # bestPercent = NumCount + zeroCount  #당첨 확률이 가장 높은 수
    # NumCount와 zeroCount를 계산하기 전에 초기화
    # 결국 초기에 0으로 설정되고 이후에 갱신되지 않기 때문에 항상 0

    NumCount = 0    #0이 아닌 숫자 중 일치하는 개수용
    zeroCount = 0   #0인 숫자의 일치하는 개수용
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}  #당첨 개수와 순위

    for i in range(len(lottos)):
        if lottos[i] in win_nums:   #일반 숫자
            NumCount += 1
        if lottos[i] == 0:  #0인 숫자
            zeroCount += 1
    bestPercent = NumCount + zeroCount
    answer = [rank[bestPercent], rank[NumCount]]  #0인 숫자가 반드시 틀릴 경우 확률이 가장 낮다
    return answer

lottos1 = [44, 1, 0, 0, 31, 25]
win_nums1= [31, 10, 45, 1, 6, 19]
print(solution(lottos1, win_nums1))

# lottos2 = [0, 0, 0, 0, 0, 0]
# win_nums2 = [38, 19, 20, 40, 15, 25] 
# print(solution(lottos2, win_nums2))

# lottos3 = [45, 4, 35, 20, 3, 9]
# win_nums3 = [20, 9, 3, 45, 4, 35]
# print(solution(lottos3, win_nums3))
