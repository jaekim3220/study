'''
덧칠하기
구역을 나누고 각 구역의 크기를 계산
롤러의 길이인 m을 활용해 최소 횟수로 덧칠할 수 있는 구역을 확인
'''

def solution(n, m, section):
    answer = 0
    for i in range(len(section)):
        # i가 0이거나 현재 구역의 번호가 이전 구역의 번호 + m보다 큰 경우
        # (현재 구역이 이전 구역에서 m만큼 떨어진 구역인 경우)
        if i == 0 or section[i] > section[i-1] + m:
            # 현재 구역은 새로운 롤러로 페인트칠 실시
            # 따라서 새로운 구역에서 페인트칠을 하는 횟수 증가
            answer += 1
    return answer

n1 = 8
m1 = 4
section1 = [2, 3, 6]
print('1번 : ',solution(n1, m1, section1))
print('-'*30)
n2 = 5
m2 = 4
section2 = [1, 3]
print('2번 : ',solution(n2, m2, section2))
print('-'*30)
n3 = 4
m3 = 1
section3 = [1, 2, 3, 4]
print('3번 : ',solution(n3, m3, section3))