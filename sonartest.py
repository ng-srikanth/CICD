def count_even_odd(n):
    count_even = 0
    count_odd = 0
    for i in range(n):
        if i%2 == 0:
            count_even += 1
        else:
            count_odd+=1
    return count_even,count_odd

print(count_even_odd(100))