info_tuple = ("zhangsan", 18, 1.75, 1.75, 1.75)

tuple = ()

print(type(info_tuple))

print(info_tuple[1])

print(info_tuple[0])

print(info_tuple.index(18))

print(info_tuple.index(1.75))
print(info_tuple.count(1.75))

print(len(info_tuple))

for my_info in info_tuple:

    print(my_info)

info_tuple_format = ("小明", 18, 1.75)

print("%s 年龄是 %d 身高是 %.2f" % info_tuple_format)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple_format

print(info_str)


num_list = [1, 2, 3, 4]
print(type(num_list))

num_tuple = tuple(num_list)
print(type(num_tuple))

print(num_tuple())

