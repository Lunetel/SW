'''
    초미세먼지 농도에 따른 문자 메세지 발송
    좋음 : 15미만
    보통 : 15 ~ 35
    나쁨 : 35초과
    
[알고리즘]
    1. 초미세먼지 농도를 측정한다.(입력받는다.)
    2. 만약 초미세먼지 농도가 15미만이면
        2-1. 좋음
    3. 만약 초미세먼지 농도가 15 ~ 35 이면
        3-1. 보통
    4. 만약 초미세먼지 농도가 35 초과이면
        4-1. 나쁨
        
'''
cho = int(input("초미세먼지 농도를 입려하시오. : "))
if cho < 15 : 
    print("좋음")
elif 15 <= cho <= 35 : 
    print("보통")
else : 
    print("나쁨") 

if cho < 15 :
    print("좋음")
if 15 <= cho <= 35 :  # mise >= 15 and mise <= 35
    print("보통")
if cho > 35 : 
    print("나쁨")
    
if cho < 15 :
    print("좋음")
elif cho <= 35 :
    print("보통")
else :
    print("나쁨")

if cho < 15 :
    print("좋음")
elif cho > 35 :
    print("나쁨")
else :
    print("보통")   