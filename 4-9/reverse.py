import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.split()
    L.reverse()
    #print(L)
    s = ''
    for w in L:
        s += w+' '
    print(s)
test_cases.close()
