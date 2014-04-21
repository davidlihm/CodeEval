import sys
real_longest = ''
longest = []
l2 = []
def copy(L):
    newL = []
    for x in L:
        newL.append(x)
    return newL
def get_possible(x1,y1, L_all):
    possible = []
    for (x2,y2) in L_all:
        if x2>x1 and y2>y1:
            possible.append((x2,y2))
    #print(possible)
    return possible
def get_sequence(longest, s1):
    s = ''
    if len(longest) ==0:
        return s
    for t in longest:
        (x,y) = t
        s += s1[x]
    return s
def get_longest(L,s1):
    for i1,i2 in L:
        L_now = [(i1,i2)]
        #print(L_now)
        L_poss = get_possible(i1,i2,L)
        #link(L_now, L_poss, L)
        get_next(L_now, L_poss,L)
            
    #print(longest)
def get_next(L_now, L_poss, L):
    global longest
    for x,y in L_poss:
        newL = copy(L_now)
        newL.append((x,y))
        poss = get_possible(x,y,L)
        #print(newL)
        if len(poss)==0:
            if len(newL) > len(longest):
                longest = copy(newL)
            #l2.append(newL)
        get_next(newL, poss, L)
        

def sub(s1,s2):
    global real_longest
    #print(len(s1))
    #print(len(s2))
    L_possible = []
    for c2 in range(len(s2)):
        for c1 in range(len(s1)):
            if s1[c1]==s2[c2]:
                L_possible.append((c1,c2))
        
    #print(L)
    get_longest(L_possible,s1)
    print(get_sequence(longest,s1))
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.split(';')
    sub(L[0],L[1][:-1])
    #sub(L[0],L[1])
    real_longest = ''

test_cases.close()
