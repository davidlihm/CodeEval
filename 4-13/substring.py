import sys
from functools import cmp_to_key

def cmp(x,y):
    a,b = x[0],y[0]
    if x[1]>a:
        a = x[1]
    if y[1]>b:
        b = y[1]
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0
def cmp2(x,y):
    a,b =x[0]+x[1], y[0]+y[1]
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0
def get_head(l1,l2):
    head,s,a,b = [],'',0,0
    length = len(l1)
    if length < len(l2):
        length = len(l2)
    for j in range(length):
        for i in range(a,len(l1)):
            for k in range(b,len(l2)):
                if l1[i] == l2[k]:
                    head.append((i,k))
        head.sort(key=cmp_to_key(cmp2))
        if len(head)>0:
            a,b = head[0]
            s += l1[a]
            #print('%d,%d' % (a,b))
            if a < len(l1)-1:
                a = a+1
            if b < len(l2)-2:
                b = b+1
        head = []    
    return s

def sub_string(s1,s2):
    print(get_head(s1,s2))

    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.split(';')
    sub_string(L[0],L[1])

test_cases.close()
