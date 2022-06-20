# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
#
#
#
# i = 1
# j = 1
# while i <= 5:
#     while j <= 5:
#         print(i*j)
#     j +=1
# i += 1


i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end = "")
        j += 1

    print("")
    i += 1

i = 1
while i <= 9:
    j = 1
    while j <= i:
    #while j <= 9:
        print("%d * %d = %d\t" % (i, j, i*j), end = "")
        j += 1

    print("")
    i += 1
