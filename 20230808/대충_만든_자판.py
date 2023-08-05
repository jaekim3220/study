'''
대충 만든 자판
할당된 문자들이 순서대로 담긴 문자열배열 keymap
입력하려는 문자열들이 담긴 문자열 배열 targets
'''

def solution(keymap, targets):
    answer = []
    keyDict = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in keyDict:   # keymap의 key의 index 번호를 추출
                keyDict[key[i]] = i+1   # i는 index=0부터 시작

    for target in targets:
        count = 0
        for t in target:
            if t not in keyDict.keys():
                count = -1
                break
            count += keyDict[t]
        answer.append(count)
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))  # [9, 4]
print(solution(["AA"], ["B"]))  # [-1]
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))  # [4, 6]