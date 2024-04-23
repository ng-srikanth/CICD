from addition import add,sub

def test_add():
    assert add(3, 5) == 8
def test_sub():
    assert sub(3,5) == -2
def test_create_duplicate():
    assert create_duplicate(4,5) == 9
def test_create_duplicate_sub():
    assert create_duplicate_sub(5,4) == 1