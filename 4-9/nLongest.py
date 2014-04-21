import sys
from functools import cmp_to_key
def cmp_len(x,y):
    if len(x)>len(y):
        return 1
    if len(x)<len(y):
        return -1
    return 0
L = []
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L.append(test)
N = int(L[0])
L2 = sorted(L[1:], key=cmp_to_key(cmp_len), reverse=True)
for e in L2[0:N]:
    print(e)

test_cases.close()
