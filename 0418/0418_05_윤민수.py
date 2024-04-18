'''
    작성일 : 2024년 4월 18일
    작성자 : 컴퓨터공학부 202495010 윤민수 
    설명 : 1부터 10까지 합을 출력하시오.
            합계를 계산하되, 합이 30이상이면 프로그램을 종료하고,
            그 때의 합을 출력하시오.
    
    [문제분석]
    반복의 조건 : 10까지
    선택의 조건 : 합이 30이상이면
    반복하면서 비교, 판단(선택)한다.
    1부터 10까지 계산을 반복하다가.....
    합계가 30이상이면 계산을 멈춘다.
    30이상일때 합계를 출력한다.
    
    break => 반복을 멈춘다. (나를 포함하고 있는 반복을 멈춘다.)
    
    [알고리즘]
    0. sum = 0
    1. 1부터 10까지 반복하면서
        1-1. 합계를 계산한다.
        1-2. 합계가 30이상이면
            1-2-1. 반복을 멈춘다. (계산을 멈춘다.)
    2. 합계를 출력한다.
    
'''
print("== for ==")
sum = 0
for num in range(1,11,1) : 
    sum = sum + num
    if sum >= 30 : 
        break   # 반복을 멈춘다.
print("sum =", sum)

print() # 빈 줄 출력

print("== while ==")
sum = 0
num = 1
while num <= 10 : 
    sum = sum + num
    if sum >= 30 : 
        break
    num = num + 1
print("sum =", sum)