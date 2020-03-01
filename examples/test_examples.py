import pytest

def datagenerator():
    l1 = [[3, 4], [6, 7], [9, 8]]
    l2 = []


    for i in range(len(l1)):
        add = l1[i][0]+l1[i][1]
        l2.append(add)
    return l2

@pytest.mark.parametrize("l2",datagenerator())
def test_sum(l2):
    print(l2)









