'''
변수 count를 0으로 초기화
hour를 0부터 N까지 반복
분(minute)을 0부터 59까지 반복(hour만 N의 영향)
초(second)를 0부터 59까지 반복(hour만 N의 영향)
시/분/초를 문자열로 변환 후  "3" 포함 유무 확인
포함되어 있다면 count를 1 증가
반복이 끝나면 count를 반환
'''

# 00:00:00 ~ N:59:59까지 3이 하나라도 포함된 경우의 수 count
def time_count(N):
    count = 0
    for h in range(N+1):  # 0부터 N까지 시간 반복
        for m in range(60):  # 0부터 59까지 분 반복
            for s in range(60): # 0부터 59까지 초 반복
                if '3'in str(h)+str(m)+str(s):
                    count+=1
    return count
N = 5
print(time_count(N))