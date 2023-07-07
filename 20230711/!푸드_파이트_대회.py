'''
물인 index=0을 제외한 나머지 음식들을 2로 나눈 몫을 구한다
몫이 두 선수가 각각 먹을 수 있는 음식의 수
몫만큼 해당 음식을 반복해 문자열로 배치
좌측 선수의 음식을 배치 후 우측 선수는 역순으로 음식의 문자열 정렬
'''

def foodFight(food):
    player1 = ''
    for i in range(1,len(food)):    #index=1부터 음식으로 인식

        player1 += str(i)*(food[i]//2)  #i번째 칼로리 음식을 몫 만큼 선수에게 전달

    result = player1 + '0' + player1[::-1]  #물은 무조건 양 선수의 중앙에 배치
    return result

food1=[1, 3, 4, 6]
print("음식배치1 : ",foodFight(food1))   # "1223330333221"

food2=[1, 7, 1, 2]
print("음식배치2 : ",foodFight(food2))   # "111303111"
