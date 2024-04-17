import pytest

def addition(a,b):
    try:
        add = a+b
        return add+"c"
    except Exception as e:
        print(e)
addition(2,3)