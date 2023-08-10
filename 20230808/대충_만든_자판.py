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

# #------------------------------
# # 인수님 풀이
# #------------------------------
def solution(keymap,targets):
    temp = [0] * len(targets)
    my_dict = dict()    
    for i in range(len(keymap)):
        for k in range(len(keymap[i])):
            if keymap[i][k] not in my_dict:
                my_dict[keymap[i][k]] = keymap[i].index(keymap[i][k]) + 1 # 몇번째 key인지 값을 넣음
            else:
                if my_dict[keymap[i][k]] > keymap[i].index(keymap[i][k]) + 1:   # 더 크면 버리고 대체
                    my_dict[keymap[i][k]] = keymap[i].index(keymap[i][k]) + 1
    for i in range(len(targets)):
        for j in range(len(targets[i])):
            if targets[i][j] in my_dict: # 타겟 값이 딕셔너리에 있다면
                temp[i] += my_dict[targets[i][j]] # 리스트의 i번째 장소에 i번째 target의 값들을 넣어서 저장
            else:
                temp[i] = -1    # 하나라도 발견이 안되면 -1로 처리
                break
    return temp