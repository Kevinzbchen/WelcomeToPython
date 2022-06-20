# 整除3，则输出fizz；整除5则输出buzz；若同时整除3和5，则输出fizzbuzz
for i in range(100):
    if i%3==0:
        if i%5==0:
            print('fizzbuzz', end=',')
        else:
            print('fizz', end=',')
    elif i%5==0:
        print('buzz', end=',')
    else:
        print(i, end=',')
