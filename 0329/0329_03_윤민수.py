'''
    작성일 : 2024년 3월 29일
    작성자 : 컴퓨터공학부 202495010 윤민수 
    설명 : 2개의 정수를 입력받아 두 수가 모두 짝수이면 더한 결과를 출력하고,
          둘 중 하나라도 홀수이면 
          몇번쨰 수를 짝수로 입력해야 하는지 알려주시오.
    
    [문제분석]
    필요한 변수는 무엇? 2개 num1 num2
    짝수는 2로 나눈 나머지가 0이다.
    홀수는 2로 나눈 나머지가 1이다.(0이 아니다.)
    두 수가 모두 짝수인가? num1 % 2 == 0, num2 % 2 == 0
    모두 짝수이면 더한 결과를 출력한다.
    두 수중 홀수가 있는가? (num1 % 2 == 1, num2 % 2 == 0), (num1 % 2 == 0, num2 % 2 == 1)
    홀수가 있다면 몇번째에 있는가?

필요한 변수 => 
[알고리즘]
    1. 두 개의 정수를 입력받는다.
    2. 두 수가 모두 짝수이면 더한 결과를 출력한다.
    3. 두 수중에 홀수가 하나라도 있으면 몇번쨰 수를 짝수로 입력해야하는지 알려준다.
'''
num1 = int(input("첫번째 수를 입력하시오. : "))
num2 = int(input("두번쨰 수를 입력하시오. : "))

# num1과 num2이 모두 짝수이다.
if num1 % 2 == 0 and num2 % 2 == 0 :
    print(f"두 수의 합은 {num1 + num2}이다.")
# 아니고 만약
elif num1 % 2 == 1 and num2 % 2 == 0 :
    print("첫번쨰 수를 짝수로 바꾸시오")
# 아니고 만약
elif num1 % 2 == 0 and num2 % 2 == 1 :
    print("두번쨰 수를 짝수로 바꾸시오.")
else : 
    print("두 수 모두 짝수로 바꿔주세요")