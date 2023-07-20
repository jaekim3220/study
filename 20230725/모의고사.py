'''
모의고사
'''
def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student1_score = 0
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student2_score = 0
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    student3_score = 0
    winner = []

    # 학생들의 패턴과 답안을 비교해 각 학생의 정답 개수를 확인
    for i, a in enumerate(answers): # index 순서와 값을 할당
        if a == student1[i % len(student1)]:    #answer의 index는 학생의 답안 패턴보다 짧거나 길 수 있음
            student1_score += 1
        if a == student2[i % len(student1)]:    #answer의 index는 학생의 답안 패턴보다 짧거나 길 수 있음
            student2_score += 1
        if a == student3[i % len(student1)]:    #answer의 index는 학생의 답안 패턴보다 짧거나 길 수 있음
            student3_score += 1
    # print(student1_score, student2_score, student3_score)

    # 가장 많은 문제를 맞힌 학생들을 winner 리스트에 추가
    max_score = max(student1_score, student2_score, student3_score)
    if student1_score == max_score:
        winner.append(1)
    if student2_score == max_score:
        winner.append(2)
    if student3_score == max_score:
        winner.append(3)

    return winner

answers1 = [1,2,3,4,5]
print('1번 : ', solution(answers1))
print("-"*30)
answers2 = [1,2,3,4,5]
print('2번 : ', solution(answers2))