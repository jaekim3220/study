def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
print(solution(["aya", "yee", "u", "maa"])) # 답:1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])) # 답:2


