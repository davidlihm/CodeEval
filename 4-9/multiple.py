import sys
def mul(s1,s2):
    a,b = int(s1),int(s2)
    larger = b 
    for x in range(1, a):       
        c = b*x
        if c >= a:
            print(c)
            return
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.split(',')
    if len(L) == 2:
        mul(L[0],L[1])

test_cases.close()
