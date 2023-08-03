'''
숫자 짝꿍 - 실패
'''

# def solution(X, Y):
#     answer = ''
#     for num in range(10):
#         count_x = X.count(str(num)) # X의 숫자를 확인
#         count_y = Y.count(str(num)) # Y의 숫자를 확인
#         count_min = min(count_x, count_y)   # 공통 숫자를 찾는 만큼 짧은걸 선택한다
#         if count_min > 0:   # 공통 숫자가 있는 경우
#             answer += str(num) * count_min  # 공통 숫자를 결과 문자열에 추가합니다. (예: 5가 3번 등장하면 '555'를 추가)

#     if not answer:  # 공통 숫자 없으면 -1 반환
#         answer = "-1"
#     else:
#         answer = ''.join(sorted(answer, reverse=True))

#     return answer

# print(solution("100", "2345"))  # -1
# print(solution("100", "203045"))    # 0
# print(solution("100", "123450"))    # 10
# print(solution("12321", "42531"))   # 321
# print(solution("5525", "1255")) # 552


#------------------------------
# 지선님 풀이
#------------------------------
def solution(X, Y):
    answer = ""       
    x_list = [0 for i in range(10)]
    y_list =  [0 for i in range(10)]
    
    
    for i in X :
        x_list[int(i)] += 1

    for j in Y :
        y_list[int(j)] += 1

    for n in range(len(x_list)-1,-1,-1):
        if x_list[n] == 0 :
            continue
        elif y_list[n] > 0 : 
            a = min(x_list[n],y_list[n])
            answer += str(n) * a

    if set(answer) == {'0'} :
        return '0'      
    elif len(answer) == 0 :
        return '-1'
    else :   
        answer = str(answer) 
        return answer

print(solution("100", "2345"))  # -1
print(solution("100", "203045"))    # 0
print(solution("100", "123450"))    # 10
print(solution("12321", "42531"))   # 321
print(solution("5525", "1255")) # 552