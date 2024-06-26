'''
    작성일 : 2024년 4월 12일
    작성자 : 컴퓨터공학부 202495010 윤민수 
    설명 : 반복문 for와  range()함수 사용법
'''
# range()함수는 범위에서 순차적인 값을 제공한다.

# 자기 이름 10개 출력하기 => 10번 출력하시오.
# 0~9까지 1씩 증가하는 값을 i변수에 저장하여 반복하시오.
for i in range(10) : 
    print(f"{i}. 윤민수")
    
print("-----------------")

# 1~10까지 출력
for i in range(1,11) :      # (초기값, 조건식 => i < 11)
    print(f"{i}. 윤민수")
    
print("-----------------")
for i in range(1,101,2) : 
    print(i, end=' ')
    
print()
for i in range(10,0,-2) : 
    print(i, end=' ')
print()
    
# 아래 그림과 같이 출력되도록 코드를 작성하시오.
'''
♥
♥ ♥
♥ ♥ ♥
♥ ♥ ♥ ♥
♥ ♥ ♥ ♥ ♥
'''
for i in range(1,6) : 
    print("♥ " * i)

print("--------------")
for i in range(5) : 
    print("♥ " * (i+1))