name_list = ["Abc", "Ghi", "Opq"]


print(name_list[0])
print(name_list[1])
print(name_list[2])

name_list.index("Abc")
print(name_list.index("Abc"))

name_list[1] = "LiSi"

name_list.append("name")

name_list.insert(0, "StartingLine")
name_list.insert(1, "SL2")

temp_list = ["wukong","tangseng"]
name_list.extend(temp_list)

name_list.pop()

name_list.pop(2)

name_list.remove("Opq")

del name_list[1]

print(name_list[0])
print(name_list)

name_list.sort()

print(name_list)

name_list.sort(reverse=True)

print(name_list[0])
print(name_list)
print(name_list.__len__())
print(len(name_list))

name_list.reverse()

print(name_list)

name_list.clear()

print(name_list)

name_list = ["A1","B2","C3","D4","E5"]

print(name_list)

for name in name_list:

    print("My name is %s" % name)



print(name_list)








