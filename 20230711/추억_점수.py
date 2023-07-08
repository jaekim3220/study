'''
프로그래머스 : 추억점수
딕셔너리를 활용한 인물별 추억 점수 저장(이름(name)과 그리움 점수(yearning)를 딕셔너리로 저장)
추억 점수를 저장할 빈 값 생성
주어진 사진에 대해 반복문 수행
사진에 등장하는 인물의 그리움 점수를 합산하기 위해 변수 초기화
사진에 등장하는 인물의 이름을 반복문을 통해 확인
딕셔너리를 이용하여 그리움 점수를 참조
해당하는 인물의 그리움 점수를 저장
모든 사진에 대해 반복문을 완료하면 결과 반환
'''

def solution(name, yearning, photo):
    answer = []
    diction = {}

    # diction에 name과 yearning의 i번째 값을 매핑해 인물별 점수 저장
    for i in range(len(yearning)):
        diction[name[i]] = yearning[i]
        # print("dictionary 값 : ", diction)

    # 이제 주어진 사진(photo)에 대해 인물의 그리움 점수를 매겨보자
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            
            if photo[i][j] in diction.keys():   #만약 photo에서 그리움을 느끼는 사람이 diction에 있다면?
                photo[i][j] = diction[photo[i][j]]  #photo[i][j]의 인물을 사용해 photo의 각 요소를 인물의 그리움 점수로 변환
                # print("photo[i][j]는 : ", photo[i][j]) #추억숫자 확인용
            else:
                photo[i][j] = 0 #photo[i][j]가 diction에 없으면? - 0으로 인식
    
    
    for i in photo: 
        answer.append(sum(i))
    
    return answer

name1 = ["may", "kein", "kain", "radi"]
yearning1 = [5, 10, 1, 3]
photo1 = [["may", "kein", "kain", "radi"],
          ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print("1번 : ",solution(name1, yearning1, photo1))

name2 = ["kali", "mari", "don"]
yearning2 = [11, 1, 55]
photo2 = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
print("2번 : ",solution(name2, yearning2, photo2))


name3 = ["may", "kein", "kain", "radi"]
yearning3 = [5, 10, 1, 3]
photo3 = [["may"],["kein", "deny", "may"], ["kon", "coni"]]
print("3번 : ",solution(name3, yearning3, photo3))