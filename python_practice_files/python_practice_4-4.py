print("나는 %d살입니다." %20)
print("나는 %s를 좋아해요." %"파이썬")
print("Apple 은 %c로 시작해요." %"A")

print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

print("나는 {}살입니다.".format(23))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="주황"))


#변수 미리 지정
age = 28
color = "보라"

print(f"나는 {age}살이며, {color}색을 좋아해요.")
#print("나는 {0}살이며, {1}색을 좋아해요.".format(age, color))