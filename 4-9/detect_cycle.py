def list_print(L):
    s = ''
    for i in L:
        s += i+' '      
    print(s[:-1])
def detect_cycle(L):
    for i in range(1,50):
        for e in range(len(L)-1-i):
            sub_l1 = L[e:e+i]
            sub_l2 = L[e+i:e+i+i]
            if sub_l1 == sub_l2:
                list_print(sub_l1)
                return

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.split()
    detect_cycle(L)

test_cases.close()
    
