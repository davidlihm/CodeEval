L_all =[]
def pmt(s,L,leng):
    #print(s)
    if len(s) == leng:
        L_all.append(s)
        return
    for c in L:
        pmt(s+c, L, leng)

def list_pmt(l,s): 
    for c in s:
        pmt(c,s,l)
def _print(l):
    s = ''
    for e in l:
        s+=e+','
    print(s[:-1])
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.strip().split(',')
    length,L2 = int(L[0]),[]
    for c in L[1]:
        L2.append(c)
    s = set(L2)
    list_pmt(length,s)
    L_all.sort()
    _print(L_all)
    L_all = []

test_cases.close()
