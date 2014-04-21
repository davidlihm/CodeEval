import sys
def fb(test):
    L = test.split(' ')[:3]
    isNumber = True
    s = ''
    A,B,N = int(L[0]),int(L[1]),int(L[2])
    if (A>20 or A<1) or (B>20 or B<1) or (N>100 or N<21):
        sys.exit(0)
    for i in range(1,N+1):
        isNumber = True
        if i%A == 0:
            isNumber = False
            s += 'F'
        if i%B == 0:
            isNumber = False
            s += 'B'
        if isNumber == True:
            s += str(i)
        s += ' '
    print(s)
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    fb(test)

test_cases.close()

