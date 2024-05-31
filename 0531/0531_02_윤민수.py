'''
    작성일 : 2024년 05월 31일
    작성자 : 컴공 202495010 윤민수
    설명 : 사용자로부터 숫자를 입력받아 그 숫자가 짝수인지 홀수인지 판별하여 반환하는 함수를 작성하고,
            이 함수를 이용하여 결과를 출력하는 프로그램을 작성하세요.
            
    [문제분석]
        사용자로부터 숫자를 입력받아 그 수가 2로 나눈 나머지가 0이면 짝수
        아니면 홀수가 나오게 한다.
        
    [알고리즘]
        [함수]
        3. 전달받은 값을 변수에 저장한다.
        4. 전달받은 num이 2로 나눈 나머지가 0이면
            4-1. 짝수
        5. 아니면
            5-1. 홀수
        6. 결과를 리턴한다.
        
        [메인]
        1. 사용자로부터 num에 숫자를 입력받는다.
        2. 그 값을 가지고 함수를 호출한다.
        7. 결과를 출력한다.
'''
def half_num(num) : 
    if num % 2 == 0 : 
        even = '짝수'
        return even
    else : 
        odd = '홀수'
        return odd
    
num = int(input("숫자를 입력하시오. : "))

print(f"입력하신 숫자는 {half_num(num)}입니다.")