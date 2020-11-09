# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# 결과: nav51!

url = "http://naver.com"
http_sliced_url = url[7:] # 규칙1
#http_sliced_url = url.replace("http://", "") # http://를 찾아서 공백으로 치환

index_first_dot = http_sliced_url.index(".") # 규칙2
before_dot_url = http_sliced_url[:index_first_dot]

first_three_url = before_dot_url[0:3] # 규칙3
num_of_letter = len(before_dot_url)
num_of_e = before_dot_url.count("e")


passwd = first_three_url + str(num_of_letter) + str(num_of_e) + "!"
print(passwd)