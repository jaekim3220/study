'''
볼링공의 무게가 주어졌을 때, 딕셔너리 또는 리스트를 사용해 각 무게의 개수를 센다
첫 번째 사람이 볼링공을 선택할 때, 두 번째 사람이 선택할 수 있는 공의 개수를 계산
    첫 번째 사람이 선택할 수 있는 볼링공의 개수는 N
    두 번째 사람이 선택할 수 있는 볼링공의 개수는 N-1
    따라서, 첫 번째 사람이 i번째 공을 선택했을 때, 
    두 번째 사람이 선택할 수 있는 볼링공의 개수는 N-i입니다.
    위의 계산을 모든 경우에 대해 반복하여 경우의 수를 누적
'''
def bowling(N,M,weights):
    count = 0 # 공을 고르는 경우의 수 초기 값
    weight_dict = {} # 공의 무게 목록(무게별 공의 개수)
    
    # 무게별 공의 개수를 dict 형태로 확인
    for a in weights:
        # print(weight_dict)
        if a in weight_dict: # dict에 해당 무게가 있으면 +1
            weight_dict[a] += 1
        else: # dict에 해당 무게가 없으면 1로 설정(초기)
            weight_dict[a] = 1

    # 공을 선택하는 경우의 수 N
    # 공의 수 N, 공의 무게 : 1~M
    for i in range(1,M+1): # 1~M
        if i in weight_dict: # i라는 무게의 공이 존재할 경우
            N -= weight_dict[i] # 선택 후 남은 공의 개수
            # 경우의 수
            count += weight_dict[i] * N  # 현재 무게의 공과 다른 무게의 공들의 조합 수
    return count
# 예시 1
N1 = 5  
M1 = 3  
weights1 = [1, 3, 2, 3, 2]  
print(bowling(N1,M1,weights1))
# 예시 1
N2 = 8  
M2 = 5  
weights2 = [1,5,4,3,2,4,5,2]  
print(bowling(N2,M2,weights2))
