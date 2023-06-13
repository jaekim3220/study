'''
첫 번째 자리의 숫자와 다음 연산에 사용될 숫자가 
0이 아닌 경우에는 *연산을 , 0인 경우에는 + 연산을 실행하는 코드
'''

def calculate(S):
    answer = int(S[0]) # 초기값은 입력한 문자열 S의 첫 번째 값
    for a in range(1, len(S)): # 1~S의 길이만큼 연산을 진행
        number = int(S[a]) # a 번째에 있는 숫자
        if number == 0 or answer==0: 
            answer += number # a번째 숫자가 0일 경우 + 연산
            # 초기 값과 a 번째(1~len(S)사이) 값이 0인 경우 + 연산을 진행
        else:
            answer *= number # a번째 숫자가 0일 경우 * 연산
    return answer
S = (0, 2, 9, 8, 4)
print(f"S 결과 : {int(calculate(S))}")
S1 = (9, 0, 2, 3, 7, 5)
print(f"S1 결과 : {int(calculate(S1))}")