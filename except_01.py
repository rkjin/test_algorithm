import numpy as np

def add(a, b):
    return a + b
def div(a, b):
    return a/b

if __name__=='__main__':
    try:
        c = add(50, 20)
        d = div(10, 0)
    except ZeroDivisionError:
        print('zero division error')

pass
  