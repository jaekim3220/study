'''
초기(시작)좌표를 설정
L은 현재 x 좌표를 1만큼 감소
R은 현재 x 좌표를 1만큼 증가
U는 현재 y 좌표를 1만큼 감소
D는 현재 y 좌표를 1만큼 증가
'''

def final_position(N, Plan):
    x, y = 1,1
    for a in Plan:
        if a == "L":
            if x > 1: #공간을 벗어나지 않게 제한
                x -= 1
        elif a == 'R':
            if x < N:
                x +=1
        elif a == 'U':
            if y > 1:
                y -= 1
        else:
            if y < N:
                y += 1
    return x,y

N = 5
Plan = ['R', 'R', 'R', 'U', 'D', 'D']
print(final_position(N, Plan))