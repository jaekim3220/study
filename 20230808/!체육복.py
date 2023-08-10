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

# #------------------------------
# # 지선님 풀이
# #------------------------------

n = 5 	# 전체학생
lost  = [3,5]	# 도난
reserve	= [2,4]	# 여벌 

# 학생들 체육복 보유 상황
students = [1 for i in range(n+1)]
for a in lost : # 도난 당한 애들 
    students[a] = 0 
for b in reserve : # 여분 있는 애들
    students[b] += 1 
real = students[1:]  
real2 = students[1:]  
#real

# 앞에서부터 없는 애들 채우기
for i in range(len(real)-1) :
    if real[i] == 0 and real[i+1] == 2 :
        real[i] = 1
        real[i+1] = 1 

for i in range(len(real)-1) :
    if real[i] == 2 and real[i+1] == 0 :
        real[i] = 1
        real[i+1] = 1 
#real

# 뒤에서부터 없는 애들 채우기 
for i in range(len(real2)-1) :
    if real2[i] == 2 and real2[i+1] == 0 :
        real2[i] = 1
        real2[i+1] = 1 
for i in range(len(real2)-1) :
    if real2[i] == 0 and real2[i+1] == 2 :
        real2[i] = 1
        real2[i+1] = 1 
#real2

# 가장 많이 채울 수 있는 걸로 사용하기
answer = n - min(real.count(0),real2.count(0))
answer