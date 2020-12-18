# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"Ham", "Spam", "Egg"}
python = set(["Ham", "Food"])

# 교집합 java + python 모두
print(java & python)
print(java.intersection(python))

# 합집합 java + python
print(java | python)
print(java.union(python))

# 차집합 java - python
print(java - python)
print(java.difference(python))

# python에 추가 됨
python.add("Cake")
print(python)

# java에서 빠짐
java.remove("Ham")
print(java)