def do(s):  
    for x1 in s:
        count = 0
        for x2 in s:
            if x1 == x2:
                count = count+1
        if count==1:
            return x1

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(do(test.strip()))

test_cases.close()
