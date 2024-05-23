'''
    작성일 : 2024년 05월 23일
    작성자 : 컴공 202495010 윤민수
    설명 : writelines()메소드 사용법
'''
# 쓰기 => write()메소드와 같은 기능을 수행하지만,
# writelines()메소드는 리스트나 튜플과 같은 자료형을 파일로 지정할 수 있다.
# 이때 리스트나 튜플로 저장된 데이터는 반드시 문자열이어야 한다.

# 리스트 생성
list1 = ['월요일\n','화요일\n','수요일\n','목요일\n','금요일\n','토요일\n','일요일\n']
list2 = [1,2,3,4,5]

# with open을 이용하여 쓰기 모드로 파일 객체 생성.
with open("text2.txt", "w") as f : 
    # 리스트의 내용을 저장.
    f.writelines(list1)
    # f.writelines(list2) # 리스트의 내용이 정수일 경우 오류가 발생한다.
    
# with open을 사용하면 f.close()를 쓸 필요 없다.