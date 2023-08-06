'''
문자열 나누기
문자열 s
분해한 문자열의 개수를 return
'''

def solution(s):
    answer = 0
    countSame = 0
    countDiff = 0

    for word in s:  #문자열 내부의 문자를 확인
        NewWord = word
        if NewWord == word: # 문자열의 문자가 첫 문자와 같다면
            countSame += 1
        else:
            countDiff += 1

        if countSame == countDiff:
            answer += 1
            
    return answer

print(solution("banana"))   # 3
print(solution("abracadabra"))   # 6
print(solution("aaabbaccccabba"))   # 3