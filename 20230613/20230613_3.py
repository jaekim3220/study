'''
연속된 숫자들을 더하는 과정에서 현재까지의 합과 최대 합을 변수로 유지하면서 숫자를 탐색
문자열을 순회하면서 숫자를 확인하고, 숫자를 만나면 현재까지의 합에 더해준다. 
숫자가 아닌 다른 문자를 만나면 현재까지의 합을 최대 합과 비교하여 더 큰 값을 최대 합으로 갱신
문자열을 모두 순회한 후에도 최대 합을 비교하여 갱신
숫자를 확인하기 위해 문자열을 한 글자씩 읽으면서 isdigit() 함수를 사용
문제를 해결하기 위해 반복문과 조건문을 사용하며, 변수를 적절히 활용
'''


def count_possible_moves(location):
    position = [(-2, 1), (-2, -1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]  # 움직일 수 있는 모든 경우의 수
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # 열 숫자 변환
    max_pos = 8  # 상하좌우 갈 수 있는 최대 위치

    row = int(location[1])
    column = columns.index(location[0]) + 1 

    count = 0
    for pos in position:
        if 0 < row + pos[0] < max_pos + 1 and 0 < column + pos[1] < max_pos + 1:
            count += 1

    return count

location = input("위치 입력 : ")
result = count_possible_moves(location)
print(result = count_possible_moves(location))
