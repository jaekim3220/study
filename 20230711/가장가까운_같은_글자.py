'''
프로그래머스 : 가장가까운_같은_글자
각 문자의 인덱스를 기록하면서 문자를 순회
순회하면서 현재 문자의 인덱스와 이전에 나온 동일한 문자들의 인덱스 차이를 계산
'''

def solution(s):
    answer = []
    word_dict = {}  # 문자와 해당 문자의 가장 최근 인덱스를 매핑할 딕셔너리
    for i in range(len(s)): 
        # print(f"word_dict는 {word_dict}.")
        # print(f"answer은 {answer}.")
        if s[i] not in word_dict:       # 현재 문자가 index_dict에 없는 경우
            answer.append(-1)   # 이전에 나온 동일한 문자가 없으므로 -1을 결과 리스트에 추가
        else:
            past_index = word_dict[s[i]]    # 현재 문자의 가장 최근 인덱스를 past_index에 저장
            answer.append(i - past_index)   # 현재 인덱스와 가장 최근 인덱스의 차이를 결과 리스트에 추가
        word_dict[s[i]] = i # 현재 문자와 해당 문자의 인덱스를 word_dict 업데이트
    return answer

s1 = "banana"
print("s1의 결과 : ",solution(s1))
s2 = "foobar"
print("s2의 결과 : ",solution(s2))
