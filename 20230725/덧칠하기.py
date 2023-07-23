'''
덧칠하기
구역을 나누고 각 구역의 크기를 계산
롤러의 길이인 m을 활용해 최소 횟수로 덧칠할 수 있는 구역을 확인
'''

#------------------------------
# 도전1
#------------------------------
# def solution(n, m, section):
#     answer = 0
#     for i in range(len(section)):
#         # i가 0이거나 현재 구역의 번호가 이전 구역의 번호 + m보다 큰 경우
#         # (현재 구역이 이전 구역에서 m만큼 떨어진 구역인 경우)
#         if i == 0 or section[i] > section[i-1] + m:
#             # 현재 구역은 새로운 롤러로 페인트칠 실시
#             # 따라서 새로운 구역에서 페인트칠을 하는 횟수 증가
#             answer += 1
#     return answer

#------------------------------
# 도전2
#------------------------------
def solution(n, m, section):
    answer = 1 # 칠하는 횟수 초기화
    paint = section[0] # 덧칠 시작점
    # 현재 구역과 이전 구역과의 거리가 m보다 크거나 같은 경우
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
            
    return answer

n1,n2,n3 = (8, 5, 4)
m1, m2, m3 = (4, 4, 1)
section1, section2, section3 = ([2, 3, 6], [1, 3],[1, 2, 3, 4])
print('1번 : ',solution(n1, m1, section1))
print('2번 : ',solution(n2, m2, section2))
print('3번 : ',solution(n3, m3, section3))