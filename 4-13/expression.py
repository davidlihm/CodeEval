import sys
def exp(o,n1,n2):
    #n1,n2 = int(n1),int(n2)
    if o == '+':
        return n1+n2
    elif o == '*':
        return n1*n2
    elif o == '/':
        return n1/n2
    else:
        raise Exception("Unknown operator: %s" % operator)
        
test_cases = open(sys.argv[1], 'r')
for test in test_cases:   
    L = test.strip().split()
    L.reverse() 
    op,num = [],[]
    result = None
    if not L:
        print(0)
    else:
        
        for c in L:
            if c.isdigit():
                num.append(int(c))      
            else:
                if result is None:
                    result = num.pop()          
                n2 = num.pop()
            #print('%d, %s, %d' % (result,c, n2))    
                result = exp(c,result,n2)
                #print(result)
            #num.append(new_num)
    print(str(int(result)))
    

test_cases.close()
