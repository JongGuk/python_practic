def power(x,y):
    if y == 0: # 5^0 = 1
        return 1

    elif y >= 1:
        res = 1
        while y > 0:
            res = res*x
            y -= 1
        return res
    
abb=power(-3,3)
print(abb)