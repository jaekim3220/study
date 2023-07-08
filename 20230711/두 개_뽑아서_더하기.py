''''
프로그래머스 : 두 개 뽑아서 더하기
두 수의 합을 저장할 빈 리스트 초기화
첫 번째 반복문에서 첫 번째 수를 추출
두 번째 반복문에서 두 번째 수를 추출
두 수의 합을 구하여 생성한 리스트에 추가
리스트를 오름차순으로 정렬
'''

def numberSum(numbers):
    answer = [] #추출할 리스트 초기화
    
    for i in range(len(numbers)):   #첫 번째 숫자 추출
        for j in range(i+1, len(numbers)):  #두 번째 숫자 추출
            number_sum = numbers[i]+numbers[j]  # 두 수의 합을 추출
            if number_sum not in answer:    #두 수를 더한 값 중 중복된 값은 배제
                answer.append(number_sum)
    answer.sort()   #오름차순 정렬
    return answer

numbers1 = [2,1,3,4,1]
print("numbers1 : ",numberSum(numbers1))
print("-"*30)
numbers2 = [5,0,2,7]
print("numbers2 : ",numberSum(numbers2))