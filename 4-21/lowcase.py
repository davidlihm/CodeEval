
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s = test.strip()
    print(s.lower())

test_cases.close()
    
