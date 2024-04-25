def count_even_odd(n):
    count_even = 0
    count_odd = 0
    for i in range(n):
        if i%2 == 0:
            count_even += 1
        elif i%2 != 0:
            count_odd+=1
        else:
            pass
    return count_even,count_odd

count_even_odd(100)