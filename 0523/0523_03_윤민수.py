'''
    작성일 : 2024년 05월 23일
    작성자 : 컴공 202495010 윤민수
    설명 : read()메소드 사용법
'''
# 읽기 = r
f = open("test.txt", "r")   # open()을 사용하여 읽기 모드로 파일 객체 f를 생성.

# 파일의 모든 내용을 읽어온다. => 변수에 저장.
texts = f.read()

# 읽어온 내용을 화면에 출력
print(texts)

f.close()   # 파일 종료