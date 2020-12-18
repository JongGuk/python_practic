# Dictionary

cabinet = {3:"Adel", 100:"Tom"}
# If not exist Key, program will print error.
print(cabinet[100])
#print(cabinet[5])

# If not exist Key, program will print "None" and keep going.
print(cabinet.get(5), "Available")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet["C-20"] = "Joy"
print(cabinet)

del cabinet[3]
print(cabinet)

# print only key
print(cabinet.keys())

# print only value
print(cabinet.values())

# print key and value
print(cabinet.items())

cabinet.clear
print(cabinet)