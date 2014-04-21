def bit_pos(num, p1,p2):
    num = bin(num)[2:]
    #print(num)
    pp1,pp2 = int(-1*p1),int(-1*p2)
    if num[pp1] == num[pp2]:
        print('true')
    else:
        print('false')

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.strip().split(',')
    bit_pos(int(L[0]),int(L[1]),int(L[2]))

test_cases.close()
