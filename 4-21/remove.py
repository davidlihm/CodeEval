import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.split(',')
    l,s = L[0].strip(),L[1].strip()
    #print(l)
    #print(s)
    newS = ''
    for c in l:
        if s.find(c)==-1:
            newS += c
    print(newS)

test_cases.close()
