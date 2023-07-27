'''
소수만들기
nums에는 중복된 숫자가 없음
'''
def solution(nums):
    answer = 0
    # 일단 3개의 수를 생성하고 더한다
    # 첫 번째 숫자를 선택
    for i in range(0, len(nums) - 2):
        # 두 번째 숫자를 선택
        for j in range(i + 1, len(nums) - 1):
            # 세 번째 숫자를 선택
            for k in range(j + 1, len(nums)):
                # 선택한 3개의 숫자를 합
                numSum = nums[i] + nums[j] + nums[k]
                
                
                # 이제 합한 숫자가 소수인지 확인
                # 합이 소수인지 확인
                # 어떤 숫자가 소수인지 확인하는 방법은
                # 그 숫자의 제곱근까지만 약수를 확인
                for a in range(2, round(numSum / 2)): 
                    if numSum % a == 0:
                # 합이 소수가 아니면
                # 확인할 필요가 없으므로 반복문에서 탈출
                        break
                else:
                    # 위의 반복문에서 소수인 경우에는 else 블록이 실행
                    # 합이 소수인 경우 answer 값을 1 증가
                    answer += 1 
    return answer


nums1, nums2 = [1,2,3,4], [1,2,7,6,4]
print("1번 : ", solution(nums1),'\n', "2번 : ", solution(nums2))