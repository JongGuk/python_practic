# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

def profile(name, age=17, main_lang="파이썬"): # 기본값을 설정할 땐 항상 뒤쪽에 위치해야 한다!
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile("유재석",-,"자바") # 생략을 위해 함수 정의시 기본값을 설정한 변수는 항상 뒤쪽에 위치해야함.
profile("김태호")
