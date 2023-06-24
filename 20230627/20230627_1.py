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
            if y > 1: #공간을 벗어나지 않게 제한
                y -= 1
        elif a == 'R':
            if y < N:
                y += 1
        elif a == 'U':
            if x > 1:
                x -= 1
        else:
            if x < N:
                x +=1
        # print(x,y)
    return x,y

N = 5
Plan = ['R', 'R', 'R', 'U', 'D', 'D']
print(final_position(N, Plan))