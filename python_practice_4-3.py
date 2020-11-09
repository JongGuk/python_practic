python = "Python is Amazing"
print(python.lower())
print(python.capitalize())
print(python.upper())
print(python[0].isupper())

a=(len(python))
print(a)

print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))
#print(python.index("Java"))

print(python.count("n"))