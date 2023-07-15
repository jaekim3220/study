'''
코딩테스트 연습 - 2016년
'''

def solution(a, b):
    # 요일 표시 (에러 해결 - 2016년 01월 01일은 '금요일'이라고 문제에서 설명 -> FRI부터 시작해야함)
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    # 각 월의 일수 표시
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 주어진 a월 이전까지의 총 일수를 계산
    # 일수들의 합에 b를 더하고, -1을 빼는 이유
    # 1월 1일은 첫 번째 날이지만, 문제에서는 0부터 시작하여 요일을 계산하기 때문에 -1 진행
    total_days = sum(month_days[:a-1]) + b - 1
    
    # 총 일수를 7로 나눈 나머지를 구하여 해당하는 요일을 반환
    # 인덱스는 0부터 시작하므로 
    # total_days % 7이 0일 경우에는 첫 번째 요일인 "FRI"를, 1일 경우에는 두 번째 요일인 "SAT"
    answer = date[total_days % 7]
    
    return answer

a = 5
b = 24
print(solution(a, b))