# # map(함수, 리스트 또는 튜플 등)
# def two_times(a):
#     return a*2
# lst = list(map(two_times, [1,2,3,4,5]))
# print(lst)
# # map, lambda 함수를 사용해 입력 list의 제곱 값을 담은 list 출력
# lst = list(map(lambda a:pow(a,2),[1,2,3,4,5]))
# print(lst)

'''M번 더하기, K번 초과 불가, 배열 크기 N'''

def maxsum(N,M,K, mylist):
    sorted(mylist, reverse=True) # 내림차순 정렬
    first_big = mylist[0] #큰 수1
    second_big = mylist[1] #큰 수2
    
    count = 0 #계산 횟 수 초기 값 = 0
    myresult = 0 #계산 값 저장소 초기 값 = 0
    while M > 0: #M은 음수 불가
        if count < K : #count=k일 경우 덧셈 중단
            myresult += first_big
            count += 1 #
        else: #큰 수2 덧셈
            myresult += second_big
            count += 1
    return myresult #결과 값 출력
print(maxsum(5,8,3, [2, 4, 5, 4, 6]))
