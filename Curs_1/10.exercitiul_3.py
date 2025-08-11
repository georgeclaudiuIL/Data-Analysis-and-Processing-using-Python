
# my_list = ["1", "2", "3", "4"] intr o singura linie de cod

print("my_list = " + str([str(x) for x in range(1,5)]))


# my_list = list(range(1,5))
# print(my_list)

my_list = list(map(str,range(1,5)))
print(my_list)