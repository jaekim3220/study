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
            # keymap의 key의 index 번호를 추출.
            # 이미 딕셔너리에 있다며 문자가 처음 등장한 인덱스 삽입
            if key[i] not in keyDict or keyDict[key[i]] > i:
                keyDict[key[i]] = i+1   # i는 index=0부터 시작
            # print("keyDict : ",keyDict)

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