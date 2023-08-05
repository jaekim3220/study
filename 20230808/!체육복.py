'''
체육수업을 들을 수 있는 학생의 최댓값을 return
전체 학생 수 n, 
도난당한 학생 번호 배열 lost, 
여벌의 체육복을 가져온 학생 번호 배열 reserve
'''
def solution(n, lost, reserve):
    answer = 0
    new_reserve = set(reserve)-set(lost)    # 빌려줄 수 있는 사람
    new_lost = set(lost)-set(reserve)   # 잃어버린 사람

    # 앞/뒤를 확인해 빌려줄 수 있는지 확인
    # 확인 후 빌려줄 수 있다면 잃어버린 사람 목록에서 제거
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)
    answer = n - len(new_lost)
    return answer

print(solution(5, [2, 4], [1, 3, 5]))   #5
print(solution(5, [2, 4], [3])) #4
print(solution(3, [3], [1]))    #2