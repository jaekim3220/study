'''
N=5로 모험가는 5명, 모험가의 공포도는 2,3,1,2,2일 경우
그룹 1에 공포도가 1,2,3인 모험가를 한 명씩 넣고,
그룹 2에는 공포도가 2인 남은 두 명을 넣게 되면,
총 2개의 그룹을 생성 가능하다
또한 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 
모든 모험가를 특정한 그룹에 넣을 필요 없음
'''


def adventure(N, fear):
    group_count = 0 # 그룹의 수
    fear.sort() # 공포도를 오름차순 정렬
    group_member = 0

    for a in fear: # 공포도가 a면 
        group_member += a # 그룹 인원은 a명
        
    if group_member >= a:
        group_count += 1
    return group_count
N = 5
fear = [2, 3, 1, 2, 2]
print(adventure(N, fear))