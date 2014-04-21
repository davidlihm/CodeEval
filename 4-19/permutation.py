import sys
import string
L_all = []
def _remove(c,s):
    news = ''
    if c==s:
        return news
    isFind = False
    for cc in s:
        if (not isFind) and (cc == c):
            isFind = True
        else:
            news += cc
    return news
def get_permutation(c,s):
    global L_all
    if s =='':
        L_all.append(c)
    new = _remove(c,s)
    for c2 in new:
        new_s = _remove(c2,new)
        get_permutation(c+c2, new_s)
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    get_permutation('',test.strip())
    L_all.sort()
    print(','.join(L_all))
    L_all = []
    #print(_remove('h','h'))
    

test_cases.close()
