'''
    작성일 : 2024년 3월 22일
    작성자 : 컴퓨터공학부 202495010 윤민수 
    설명 : 5과목의 점수를 입력받아 합계와 평균을 출력하는 프로그램을 작성하시오.
    
    [문제분석]
    5과목의 점수를 입력받는다.
5과목의 합계 = 국어 + 수학 + 컴퓨터 + 과학 + 영어 = ?
5과목의 평균 = 5과목의 합계/5



필요한 변수 => kor(국어), math(수학), com(컴퓨터), sci(과학), eng(영어), total(5과목의 합), avg(평균)

[알고리즘]
1. 국어 점수를 입력받는다.
2. 수학 점수를 입력받는다.
3. 컴퓨터 점수를 입력받는다.
4. 과학 점수를 입력받는다.
5. 영어 점수를 입력받는다.
6. 5과목의 합을 구한다.
7. 5과목의 평균을 구한다.
'''
#5과목의 점수를 입력받아 각각 변수에 저장하시오.
kor = int(input("국어 점수를 입력하시오. : "))
math = int(input("수학 점수를 입력하시오. : "))
com = int(input("컴퓨터점수를 입력하시오. : "))
sci = int(input("과학 점수를 입력하시오. : "))
eng = int(input("영어 점수를 입력하시오. : "))

# 5과목의 점수를 합하여 변수에 저장하시오.
total = kor + math + com + sci + eng

#5과목의 합계를 출력하시오.
print(f"5과목의 합은 {total}입니다.")

# 5과목의 평균 구하기.
avg = total/5
print(f"5과목의 평균은 {avg}입니다.")