import sys
def parse(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return True   
    index_s2 = 0
    for i,c in enumerate(s2):
        if c =='\\' and s2[i+1] =='*':
            isHaveStar= False
            starPosition = None
            for i3,c3 in enumerate(s1):
                if c3 =='*':
                    if not isHaveStar:
                        starPosition = i3
                    isHaveStar = True                 
            if  isHaveStar:
                return parse(s1[starPosition+1:],s2[i+2:])
            else:
                
                return False
                
        elif c=='*':
            if i==0:
                return parse(s1,s2[1:])
                return parse(s1, s2[:i]) and parse(s1,s2[i+1:])
        else:
            b = False
            for ii,cc in enumerate(s1):                   
                if cc==c:
                    b=True
                    if i==len(s2)-1:
                        return True
                    else:
                        return parse(s1[ii+1:], s2[i+1:])
            return b
            
def sub(s,p):
    for i,c in enumerate(s):
        if c == p[0]:
            for i2,c2 in enumerate(p[1:]):
                if c2 != s[i+1+i2]:
                    return False
    return True

def change(b):
    if b:
        print('true')
    else:
        print('false')
#print('C\*Eval'.find('\\'))
test_cases = open(sys.argv[1], 'r')
#print(len('C\*Eval'))
for test in test_cases:
    L = test.strip().split(',')
    #print(sub(L[0],L[1]))
    change(parse(L[0],L[1]))

test_cases.close()
