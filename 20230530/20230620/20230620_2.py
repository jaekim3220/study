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
    count = 0 # 볼링공을 고르는 경우의 수 초기 값
    weight_dict = {} # 공의 무게 목록(무게별 공의 개수)
    
    # 무게별 공의 개수를 dict 형태로 확인
    for a in weights:
        print(weight_dict)
        if a in weight_dict:
            weight_dict[a] += 1
        else:
            weight_dict[a] = 1
    return weight_dict
weights = [1, 3, 2, 3, 2] 
print(bowling(weights))