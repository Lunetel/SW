'''
    10개의 숫자를 입력받아,
    0보다 큰 수에 대해서만 전체 합과 평균을 출력하는 프로그램을
    while문을 사용하여 작성하시오.
    
    sum = 0 잊지말자~~~!!!
    
    10개의 숫자를 입력 받는다.
    10번 반복하면서 숫자를 입력 받으면서 양수인지 확인하고,
    양수이면 합계를 계산한다.
    음수이면 아무것도 할 필요가 없다. 신경쓰지 말자!
    
    합계가 다 계산되면 평균 계산하면 된다.
    
    반복 [ 선택
    
    [알고리즘]
        0. count = 0    => 양수일 때 개수 증가
        1. sum = 0 초기값 지정.
        2. 10번 반복하면서
            2-1. 숫자를 입력받는다.
            2-2. 양수인가? 판단
                2-2-1. 합계를 계산한다.
                2-2-2. count = count + 1
        3. 평균을 계산한다.
        4. 합계를 평균 출력
'''
count = 0
sum = 0

for i in range(10) : 
    num = int(input("정수입력 : "))
    
    if num > 0 : 
        sum = sum + num
        count += 1      # count = count + 1

avg = sum / count
print("합계 : ", sum)
print("평균 : ", avg)

print("=====================================")

count = 0
sum = 0

while True :    # 무한반복
    num = int(input(str(count+1)+ "번째 정수 입력 : "))
    
    if num > 0 : 
        sum = sum + num
        count += 1
        
    if count >= 10 :     # 이 조건을 만족하면 반복은 종료된다.
        break       # 반복을 멈춘다.
    
avg = sum / count
print("합계 : ", sum)
print("평균 : ", avg)