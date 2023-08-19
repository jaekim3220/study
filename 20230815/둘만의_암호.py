'''
a~z까지의 알파벳에서 skip에 포함된 문자는 제거 후
문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 교체
'''

def solution(s, skip, index):
    answer = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    for i in skip:  # 문자가 skip에 포함된 경우
        if i in s:
            answer = answer.replace(i,"")   # skip에 포함된 문자 삭제,str은 pop 사용 불가
            
    
    for j in s:
        result += answer[(answer.index(j) + index) % len(answer)]

    return result

print((solution("aukks", "wbqd", 5)))   #"happy"