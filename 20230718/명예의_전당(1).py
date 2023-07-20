'''
코딩테스트 연습 - 명예의 전당(1)
score 리스트를 순회하면서 현재까지의 점수를 정렬
정렬된 점수 리스트에서 최하위 점수를 추출(index=0)
추출한 최하위 점수를 answer 리스트에 추가
'''

def solution(k, score):
    answer = [] #명예의 전당 값 저장 list
    score_list=[]   #점수들을 저장할 list
    for s in score:
        if len(score_list) < k: #점수저장 list에 자리가 남았을 때
            score_list.append(s)
        else: #점수저장 list에 자리가 없는 경우
            if min(score_list)<s: # 새 점수가 저장된 점수 최소값 보다 크다면
                score_list.remove(min(score_list))  #저장된 최소 점수 빼기
                score_list.append(s)    #새로운 점수 추가
        # min(score_list)이 아닌 (score_list)를 입력해서 에러가 발생한 거였음
        answer.append(min(score_list))   #명예의 전당 값에 최소 점수 입력
    return answer

k1 = 3
score1 = [10, 100, 20, 150, 1, 100, 200]
print("1번 : ",solution(k1, score1))
print("-"*30)
k2 = 4
score2 = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
print("2번 : ",solution(k2, score2))