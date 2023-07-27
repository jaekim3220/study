#------------------------------
# 지선님 풀이
#------------------------------

# 소수 판별 함수
def is_prime_number(x):
    for i in range(2, int((x)** (1/2)) + 1):
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

n = 5 
cnt = 0
for i in range(2,n+1) :
    if is_prime_number(i) :
        cnt += 1
cnt

n1 = 10
n2 = 5
print("1번 :",is_prime_number(n1))
print("2번 :",is_prime_number(n2))