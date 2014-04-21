L = []
num = 0
for i in range(7):
    for x in range(2**i-1):
        s = ''
        n = bin(x)[2:]
        if i>1:
            for ii in range(i-len(n)):
                s += '0'
            s+=n
        else:
            s = n
        L.append(s)


def decode(s,p):
    if p[-3:]=='000':
        p = p[:-3]
    key = []
    output = ''
    # map string to key
    for i,c in enumerate(s):
        key.append((L[i],c))
    while p!= '':     
        #print(p)
        l,p=int(p[:3],2),p[3:]
        stop = ''
        for i in range(l):
            stop+='1'
        #print(stop)
        #stop_p : stop position
        #stop_p = p.find(stop)
        #sub = p[:stop_p]
        #sub: keys
        if l>0:
            for i in range(0,len(p),l):
                subkey = p[i:i+l]
                if subkey==stop:
                    p=p[i+l:]
                    break
                for k in key:
                    if k[0] == subkey:
                        #print(k)
                        output += k[1]
                        break
        
        #print(output)
    print(output)
    
def test_decode(s,p):
    print(s)
    
import sys
test_cases = open(sys.argv[1], 'r')
temp = ''
for test in test_cases:
    s = test.strip()
    for i2,x in enumerate(s):
                    if x=='0' or x=='1':
                        a,b = s[:i2],s[i2:]
                        decode(a,b)
                        break
    
'''
for test in test_cases:
    temp += test.strip()
    leng = len(temp) 
    for i in range(leng):
        if i>2:
            if (i==leng-1) or(temp[i-1]=='0' or temp[i-1]=='1') and (temp[i] != '0' and temp[i] != '1'):
                s = temp[:i+1]
                for i2,x in enumerate(s):
                    if x=='0' or x=='1':
                        a,b = s[:i2],s[i2:]
                        decode(a,b)
                        break
                temp = temp[i+1:]
                break'''

test_cases.close()
