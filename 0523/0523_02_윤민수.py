'''
    작성일 : 2024년 05월 23일
    작성자 : 컴공 202495010 윤민수
    설명 : append()메소드 사용법
'''
# 추가 = a
f = open("test.txt", "a")   # open()을 사용하여 파일 객체 f를 생성.

# 파일에 추가 할 내용 작성.
f.write("추가 메세지입니다. \n")

f.close()   # 파일 종료