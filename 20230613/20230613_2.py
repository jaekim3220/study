'''
첫 번째 자리의 숫자와 다음 연산에 사용될 숫자가 
0이 아닌 경우에는 *연산을 , 0인 경우에는 + 연산을 실행하는 코드
'''

def calculate(S):
    answer = int(S[0]) # 초기값은 입력한 문자열 S의 첫 번째 값
    for a in range(1, len(S)): # 1~S의 길이만큼 연산을 진행
        if a != 0:
            answer *= a
        else:
            answer += a
    return answer
S = (0, 2, 9, 8, 4)
print(int(calculate(S)))