'''
a~z까지의 알파벳에서 skip에 포함된 문자는 제거 후
문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 교체
'''

def solution(s, skip, index):
    answer = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    for i in skip:  # 문자가 skip에 포함된 경우
        if i in answer: # skip에 포함된 문자가 answer에 있으면
            answer = answer.replace(i,"")   # skip에 포함된 문자 삭제,str은 pop 사용 불가
            
    for j in s:
        result += answer[(answer.index(j) + index) % len(answer)]   #% len(answer)을 통해 answer의 범위를 벗어나는 것을 방지
    # print("answer길이:",len(answer))
    return result

print((solution("aukks", "wbqd", 5)))   #"happy"