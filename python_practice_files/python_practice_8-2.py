# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0:_<+10}".format(500))

print("{0:,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))
print("{0:-<+22,}".format(1000000000000))

print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))