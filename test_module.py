from addition import add,sub,count_even_odd

def test_add():
    assert add(3, 5) == 8
def test_sub():
    assert sub(3,5) == -2

def test_count_even_odd():

    assert count_even_odd(101) == (51, 50), "Test case failed"