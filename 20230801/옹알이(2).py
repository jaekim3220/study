def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:   #발음할 수 있는 단어를 사용
            if j*2 not in i:    #같은 단어를 2번 말하는건 시작부터 제외
                i=i.replace(j,' ')  #옹알이에 발음 할 수 있는 단어가 있다면 공백으로 변경
        if len(i.strip())==0:   #발음할 수 있는 단어를 합쳐서 말을 했으면 공백만 남을 것
            answer +=1
    return answer
print(solution(["aya", "yee", "u", "maa"])) # 답:1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])) # 답:2