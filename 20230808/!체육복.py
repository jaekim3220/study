def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1): # 학생 수만큼
        if i in lost:   # 잃어버린 학생 기준
            if i+1 in reserve:  
                answer += 1
            elif i-1 in reserve:
                answer += 1
    return answer

print(solution(5, [2, 4], [1, 3, 5]))   #5
print(solution(5, [2, 4], [3])) #4
print(solution(3, [3], [1]))    #2