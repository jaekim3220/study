'''숫자 카드 게임
각 행에서 가장 작은 숫자를 찾는다
가장 작은 숫자들 중에서 가장 큰 숫자를 선택한다'''

'''카드 리스트가 주어지는 경우'''
def card(mycards): 
    card_list = [] # 각 행의 최소 값 저장 list
    for a in mycards: # 입력 받은 'mycards 내부 요소'를 card_list에 입력 해야 함
        card_list.append(min(a)) # 추출한 최소 값을 card_list에 입력
    return max(card_list) # card_list에서 가장 큰 값을 출력

cards1 = [[3, 1, 2], 
         [4, 1, 4], 
         [2, 2, 2]]
print(f"결과 : {card(cards1)}")

cards2 = [[8, -80, 23], 
         [23, 71, -10], 
         [-5, 100, 86]]
print(f"결과 : {card(cards2)}")
