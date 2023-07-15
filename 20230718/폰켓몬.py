'''
코딩테스트 연습 - 폰켓몬
중복을 제거하기 위해 Set을 사용하여 중복을 제거한 폰켓몬 종류의 수 확인
중복을 제거한 폰켓몬 종류의 수와 N/2 중 작은 값을 선택해 최댓값 추출
'''

def solution(nums):
    # 중복을 제거한 폰켓몬 종류의 수를 확인
    unique_nums = set(nums)
    # print("unique_nums : ",unique_nums)

    # 이제 폰켓몬을 선택할 수 있는 종류의 수의 최댓값을 확인
    # N/2마리의 폰켓몬을 선택하여 가장 많은 종류의 폰켓몬을 선택
    # -> 선택할 수 있는 폰켓몬 `종류`의 개수를 최대로 유도
    maxCase =  min(len(unique_nums), len(nums) // 2)

    return maxCase

nums1 = [3,1,2,3]
print("1번 : ", solution(nums1))
nums2 = [3,3,3,2,2,4]
print("2번 : ", solution(nums2))
nums3 = [3,3,3,2,2,2]
print("2번 : ", solution(nums3))