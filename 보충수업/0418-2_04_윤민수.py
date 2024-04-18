'''
정수를 입력받아 그 수가 소수인지 아닌지 판별하시오.

[문제분석]
    소수는 1과 자기자신으로 나누어 떨어지는 수(나누어 나머지가 0인 수)
    
    1을 제외하고 2부터 자기자신까지 나누어 나머지가 0인 것을 확인하자.
    
    반복조건 : 자기자신까지(입력 수까지)
    선택조건 : 나누어 나머지가 0이면
    
    [알고리즘]
        1. 정수를 입력받는다.
        2. 2부터 입력받은 수까지 반복하면서
            2-1. 입력수를 2부터 나누어 나머지가 0이면
                2-1-1. 반복을 멈춘다.
        # 반복이 끝나면 (멈추면)
        3. 입력받은 수와 나누는 수가 같으면
            3-1. 00은 소수이다.
        4. 아니면
            4-1. 00은 소수가 아니다.

'''
input_num = int(input("정수 입력 : "))

for num in range(2, input_num + 1) : 
    if input_num % num == 0 : 
        break
        
if input_num == num :   # 입력 수와 나누는 수가 같으면
    print(f"{input_num}은 소수입니다.")
else : 
    print(f"{input_num}은 소수가 아닙니다.")

