'''
첫 번째 자리의 숫자와 다음 연산에 사용될 숫자가 
0이 아닌 경우에는 *연산을 , 0인 경우에는 + 연산을 실행하는 코드
'''

def calculate(S):
    answer = 0
    for a in range(len(S)):
        if a != 0:
            answer *= a
        else:
            answer += a
    return answer
S = (0, 2, 9, 8, 4)
print(int(calculate(S)))