import random as rand

def quick_sort(the_list, start, end):
    if start < end:
        m, n = start, end
        base = the_list[m]
        while m < n:
            while (m < n) and (the_list[n] >= base):
                n = n - 1
            the_list[m] = the_list[n]
            while (m < n) and (the_list[m] <= base):
                m = m + 1
            the_list[n] = the_list[m]
        the_list[m] = base
        quick_sort(the_list, start, m-1)
        quick_sort(the_list, n+1, end)
    return the_list

if __name__ == '__main__':
    the_list = [rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999)]
#    the_list = [rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999),rand.randint(1,999)]
    start = 0
    end = len(the_list) - 1
    print(the_list)
    print(quick_sort(the_list, start, end))
