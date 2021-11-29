import numpy as np

if __name__ == '__main__':
    try:
        f = open('test_file.txt', 'w')
        f.write('this is exception finally')
    except Exception as e:
        pass
    finally:
        f.close


pass
