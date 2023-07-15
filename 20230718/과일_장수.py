'''
이익을 가장 크게 내기 위해서는 내림차순 정렬 후 큰 수를 뽑도록 유도 
1~k 등급, m개씩 선별
'''

def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)

    for s in range(0, len(score), m):   #선별한 오름차순 과일을 m개씩 분리
        score_list = score[s : s+m] #선별된 과일 집단
        if len(score_list) == m:    # m개의 점수가 할당된 경우에만 계산
            # 점수 리스트에서 최솟값을 선택
            # 선택한 최솟값을 m번 곱함
            # m개 모두 최소 값만큼 점수 부여하기 때문 때문
            answer += min(score_list) * m 
    return answer

k1 = 3	
m1 = 4	
score1 = [1, 2, 3, 1, 2, 3, 1]
print("1번 : ",solution(k1, m1, score1))

k2 = 4
m2 = 3
score2 = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print("2번 : ",solution(k2, m2, score2))
