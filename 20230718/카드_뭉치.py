def solution(cards1, cards2, goal):
    answer = ''
    for g in goal:
        
        if len(cards1)>0 and g == cards1[0]:
            answer += cards1[0]
            cards1.pop(0)
            
        elif len(cards2)>0 and g == cards2[0]:
            answer += cards2[0]
            cards2.pop(0)
        else:
            return "No"
        
        # print(answer)
    
    return "Yes"

cards1_1 = ["i", "drink", "water"]
cards2_1 = ["want", "to"]	
goal_1 = ["i", "want", "to", "drink", "water"]
print("1번 : ", solution(cards1_1, cards2_1, goal_1))
print("-"*30)
cards1_2 = ["i", "water", "drink"]
cards2_2 = ["want", "to"]	
goal_2 = ["i", "want", "to", "drink", "water"]
print("2번 : ", solution(cards1_2, cards2_2, goal_2))