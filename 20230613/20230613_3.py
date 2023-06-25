def count_min(info_number):
    number0 = 0  
    number1 = 0  

    if info_number[0] == '0':
        number0 += 1 
    else:  # 1로 시작되면
        number1 += 1 

    for i in range(len(info_number) - 1):  # 문자 길이만큼 반복 (out of range 조심)
        if info_number[i] != info_number[i + 1]:  # 앞 숫자와 뒷 숫자가 다르면
            if info_number[i] == '0':  # 앞이 0이고 뒷 숫자랑 다르면
                number1 += 1 
            else:  # 앞이 1인데 뒷 숫자랑 다르면
                number0 += 1 

    return min(number0, number1) 

info_number = '0001100'
print(count_min(info_number))