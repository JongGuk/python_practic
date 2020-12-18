# print("Python", "Java", "JavaScript", sep=" vs ")
# print("Python", "Java", sep=",", end="? \t")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# scores = {"Math":0, "English":50, "Coding":100} # Dict
# for subject, score in scores.items(): # Tuple
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # input 으로 받은 값은 항상 str 이다!
print("입력하신 값은 " + answer + "입니다.")