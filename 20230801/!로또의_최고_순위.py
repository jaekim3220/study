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

    NumCount = 0    #알 수 있는 숫자 중 일치하는 개수
    zeroCount = 0   #모르는 숫자 중 일치하는 개수
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}  #당첨 개수와 순위

    for i in range(len(lottos)):
        if lottos[i] in win_nums:   #일반 숫자
            NumCount += 1
        if lottos[i] == 0:  #0인 숫자
            zeroCount += 1
    bestPercent = NumCount + zeroCount
    answer = [rank[bestPercent], rank[NumCount]]  #0인 숫자가 반드시 틀릴 경우 확률이 가장 낮다
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25] ))

print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

#------------------------------
# 지선님 풀이
#------------------------------

lottos = [1, 2, 3, 4, 5, 6]
win_nums = [7, 8, 9, 10, 11, 12]	 # result [3, 5]

min_cnt = 0
for i in lottos :
    if i in win_nums :
        min_cnt += 1

max_cnt = lottos.count(0)

if min_cnt == 0 :
    answer = [7-max_cnt,7-1]
if answer[0] == 7 :
    answer = [6,6]
else :
    answer = [7-(max_cnt+min_cnt),7-min_cnt]
answer