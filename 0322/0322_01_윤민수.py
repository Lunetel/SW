'''
    작성일 : 2024년 3월 22일
    작성자 : 컴퓨터공학부 202495010 윤민수 
    설명 : 입력 input()함수 사용하기
'''
# 이름을 입력받아 변수에 저장하시오.
name = input("이름을 입력하시오 : ")

# 입력받은 이름을 출력하시오.
# OO님 환영합니다.

print(name, "님 환영합니다.")

# 국어점수와 수학점수를 입력받아 각각 변수에 저장하시오.
kor = input("국어점수 입력 : ")
math = input("수학점수 입력 : ")

# 두 과목의 점수를 합하여 변수에 저장하시오.
sum = kor + math

# 두 과목의 합계를 출력하시오.
# 두 과목의 점수의 합계는 OO점 입니다.
print("두 과목의 합계는", sum, "점 입니다.")
print("두 과목의 합계는 {}점 입니다.".format(sum))
print(f"두 과목의 합계는 {sum}점 입니다.")

# 영어점수와 컴퓨터 점수를 입력받아 정수로 변환하여 변수에 저장.
eng = int(input("영어점수 입력 : "))
com = int(input("컴퓨터 점수 입력 : "))


# 두 과목의 점수 합계를 계산하시오.
sum = eng + com
# 두 과목의 합계를 출력하시오.
# 두 과목의 점수의 합계는 OO점 입니다.
print("두 과목의 합계는", sum, "점 입니다.")
print("두 과목의 합계는 {}점 입니다.".format(sum))
print(f"두 과목의 합계는 {sum}점 입니다.")
