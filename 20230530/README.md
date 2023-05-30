코딩 테스트 p92 실전문제 1 : 큰 수의 법칙

수정1
mylist를 myarr로 변경, 정렬 확인을 위해 print(myarr) 추가
확인 결과 
sorted(myarr, reverse=True)
print(myarr)
로는 정렬이 되지 않음
-> sorted(myarr, reverse=True)를 myarr = sorted(myarr, reverse=True) 로 변경
결과 : 동작 X

수정2
else: #큰 수2 덧셈
            myresult += second_big
            count += 1 일 경우 큰 수2가 최대 합에 더해지는 횟수가 증가
        ->  count = 0 
결과 : 배열 정렬 값 print