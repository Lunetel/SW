'''
    작성일 : 2024년 05월 23일
    작성자 : 컴공 202495010 윤민수
    설명 : readline()메소드 사용법
'''
print("== readline()메소드를 이용하여 읽기 ==")

# readline()메소드는 주로 while 반복문과 함께 사용

# with open을 이용하여 읽기 모드로 파일 객체 생성.
with open("text2.txt", "r") as f : 
    # while문을 사용하여 무한 반복
    while True : 
        line = f.readline() # 한 줄씩 읽어와서 변수에 저장.
        print(line) # 내용 출력.
        
        if line == '' :     # 읽어온 값이 없는 경우 반복을 벗어난다.
            break
    
# with open을 사용하면 f.close()를 쓸 필요 없다.