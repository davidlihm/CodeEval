import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.split()
    L.reverse()
    s = ''
    for i in range(len(L)):
        if i%2 ==0:
            s += L[i]+' '
    print(s)

test_cases.close()
