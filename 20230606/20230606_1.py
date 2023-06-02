'''숫자 카드 게임
각 행에서 가장 작은 숫자를 찾는다
가장 작은 숫자들 중에서 가장 큰 숫자를 선택한다'''
def card(mycards): 
    card_list = [] # 각 행의 최소 값 저장 list
    for a in mycards: # 입력 받은 'mycards 내부 요소'를 card_list에 입력 해야 함
        card_list.append(a) # 추출한 값을 card_list에 입력
    return card_list
