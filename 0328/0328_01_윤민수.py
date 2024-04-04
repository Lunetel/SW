'''
    작성일 : 2024년 3월 28일
    작성자 : 컴퓨터공학부 202495010 윤민수 
    설명 : 성적을 입력받아 80점 이상이면 "당신의 점수는 00점입니다."
          "좋은 성적입니다."를 출력하는 프로그램을 작성하시오.
    
    [문제분석]
    필요한 점수는 무엇? 점수 저장 변수: score/jumsu
    점수는 80점 이상이어야 한다.
    입력받은 점수가 80점 이상인가?
    80점 이상이면 메세지를 출력한다.
    점수를 입력받는다. -> 정수로 변환 -> 변수에 저장.



필요한 변수 => 
[알고리즘]
    1. 점수를 입력받는다.
    2. 점수가 80점 이상이면
        2-1 "당신의 점수는 00점입니다."
            "좋은 성적입니다."
    3. "감사합니다." 출력한다.
        => 조건과 상관없이 무조건 출력
'''
score = int(input("점수를 입력하시오. : "))

if score >= 80 :
    print(f"당신의 점수는 {score}점입니다. ")
    print("좋은 성적입니다.")
    
print("감사합니다.")
    