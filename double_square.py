def dsq(count,x):
    n,L = 0,[]
    for n1 in range(100):
        for n2 in range(100):
            sqrt = n1**2 + n2**2
            if sqrt>x:
                
                        
    
import sys
test_cases = open(sys.argv[1], 'r')
for i,test in enumerate(test_cases):
    if i>0:
        s = int(test.strip())
        dsq(0,s)

test_cases.close()
