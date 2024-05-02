'''
    작성일 : 2024년 05월 02일
    작성자 : 컴퓨터공학부 202495010 윤민수
    설명 : 2. 사용자로부터 시작 값과 끝 값을 입력받아
              두 수 사이의 전체 합계와
              짝수의 합계,
              홀수의 합계를 출력하시오.
    
   [문제분석]
        2개의 정수를 입력 받는다.
        두 수를 포함하여 두 수 사이의 모든 수의 합계를 계산한다.
        두 수 사이의 짝수와 홀수를 판단하여 각각 합계 계산한다.
        
        짝수는 2로 나눈 나머지가 0이다.
        홀수는 2로 나눈 나머지가 0이 아니다.
        
        입력받은 두 수 사이를 반복하면서 합계를 계산한다.
        
        num1 < num2 부터 num2까지 1씩 증가하면서...
        num1 > num2 ???
                => 1) num1부터 num2 까지 1씩 감소하면서...
                => 2) num2부터 num1 까지 1씩 증가하면서...
                => 3) 두 변수의 값을 교환한다.
                => 4) 사용자에게 첫번째 값은 작은 값, 두번째 값은 큰 값으로 입력하도록 가이드 준다.
        
   [알고리즘]
       1. 두 정수를 입력받는다.
       2. 전체 합계, 짝수 합계, 홀수 합계, 변수 초기화
       3. 만약 num1 < num2 이면
        3-1. num1부터 num2까지 1씩 증가하면서
            3-1-1. 합계를 계산한다.
            3-1-2. 수가 짝수이면
                3-1-2-1. 짝수의 합계를 계산한다.
            3-1-3. 아니면
                3-1-3-1. 홀수의 합계를 계산한다.
       4. 아니면 (num1 > num2)
        4-1. num2부터 num1까지 1씩 증가하면서..
            4-1-1. 합계를 계산한다.
            4-1-2. 수가 짝수이면
                4-1-2-1. 짝수의 합계를 계산한다.
            4-1-3. 아니면
                4-1-3-1. 홀수의 합계를 계산한다.
       5. 결과 출력
'''
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))

total_sum = 0     # 합계 계산 변수 초기화
even_sum = 0        # 짝수 합계
odd_sum = 0         # 홀수 합계

if num1 < num2 : 
    for num in range(num1, num2 + 1) : 
        total_sum += num      # sum = sum + num
    if num % 2 == 0 :   # 짝수이면
        even_sum += num
    else :      # 홀수이면
        odd_sum += num
else : # num1> num2
    for num in range(num2, num1 + 1) : 
        total_sum += num      # sum = sum + num
    if num % 2 == 0 :   # 짝수이면
        even_sum += num
    else :      # 홀수이면
        odd_sum += num
        
print(f"{num1}부터 {num2}까지 전체 합 : {total_sum}")
print(f"{num1}부터 {num2}까지 짝수 합 : {even_sum}")
print(f"{num1}부터 {num2}까지 홀수 합 : {odd_sum}")

'''
[알고리즘]
       1. 두 정수를 입력받는다.
       2. 전체 합계, 짝수 합계, 홀수 합계, 변수 초기화
       3. 만약 num1 < num2이면
        3-1. 두 수를 교환한다. (작은 수, 큰 수)
       4. num1부터 num2까지 1씩 증가하면서
        4-1. 합계를 계산한다.
        4-2. 스기 짝수이면
            4-2-1. 짝수의 합계를 계산한다.
        4-3. 아니면
            4-3-1. 홀수의 합계를 계산한다.
        5. 결과를 출력한다.
'''
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))

total_sum = 0     # 합계 계산 변수 초기화
even_sum = 0        # 짝수 합계
odd_sum = 0         # 홀수 합계

# 두 정수 값 교환
if num1 > num2 : 
    num1, num2 = num2, num1
for num in range(num1, num2 + 1) : 
    total_sum += num      # sum = sum + num
    if num % 2 == 0 :   # 짝수이면
        even_sum += num
    else :      # 홀수이면
        odd_sum += num
    
print(f"{num1}부터 {num2}까지 전체 합 : {total_sum}")
print(f"{num1}부터 {num2}까지 짝수 합 : {even_sum}")
print(f"{num1}부터 {num2}까지 홀수 합 : {odd_sum}")
