# # List

# # Each subway contain 10, 20, 30 person.

# subway1 = 10
# sunway2 = 20


# subway = [10, 20, 30]
# print(subway)

# subway = ["Adel", "Tom", "Joy"]
# print(subway)

# # where is Adel?
# print(subway.index("Adel"))

# # Gray get on subway at the next station in lastest car.
# subway.append("Gray")
# print(subway)

# # Michelle get on subway at between Adel and Tom.
# subway.insert(1, "Michelle")
# print(subway)

# # Take off person from lastest car.
# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # Find how many person which has same name.
# subway.append("Adel")
# print(subway)
# print(subway.count("Adel"))

# # Ordering
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

num_list = [5,2,4,3,1]
mix_list = ["Adel", 20, True]

num_list.extend(mix_list)
print(num_list)