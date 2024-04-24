def add(x, y):
    if x < 0:
        return x - y
    else:
        return x + y
def sub(x, y):
    return x - y

def count_even_odd(n):
    count_even = 0
    count_odd = 0
    for i in range(n):
        if i%2 == 0:
            count_even+=1
        elif i%2!=0:
            count_odd += 1
        else:
            pass
    return count_even,count_odd
add(1, 2)
sub(2, 2)
count_even_odd(100)
