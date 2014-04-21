
class Node(object):
    def __init__(self, v, l,r,p,d):
        self.value = v
        self.left = l
        self.right = r
        self.parent = p
        self.deep = d

def find(root,value):
    if root == None:
        return 
    if root.value == value:
        return root
    else:
        if value < root.value:
            #print(root.left.value)
            return find(root.left,value)
        else:
            #print(root.right.value)
            return find(root.right,value)
    #return None
'''
def find(root,value):
    if root == None:
        return 
    if root.value == value:
        return root
    else:
        if root.left is not None:
            print(root.left.value)
            find(root.left,value)
        if root.right is not None:
            print(root.right.value)
            find(root.right,value)
    #return None'''
    
node = Node(30,None,None,None,0)
node.left = Node(8,None,None,node,1)
node.right = Node(52,None,None,node,1)
node.left.left = Node(3,None,None,node.left,2)
node.left.right = Node(20,None,None,node.left,2)
node.left.right.left = Node(10,None,None,node.left.right,3)
node.left.right.right = Node(29,None,None,node.left.right,3)
def isParent(root, v):
    n = find(root, v)
    if n is None:
        return False
    return True
    
    
    
def find_lowest(n1,n2,node,lowest): 
    pt = find(node,n1).parent
    #if pt is not None:
        #print(pt.value)
    while pt is not None:
        if isParent(pt, n2):
            #print(pt.value)
            if pt.deep>lowest[1]:
                #print('%d,%d' % (pt.deep,pt.value))
                lowest = (pt.value,pt.deep)
        pt = pt.parent
    pt = find(node,n2).parent
    while pt is not None:
        if isParent(pt, n1):
            if pt.deep>lowest[1]:
                #print('%d,%d' % (pt.deep,pt.value))
                lowest = (pt.value,pt.deep)
        pt = pt.parent
    print(lowest[0])   
    #print(pt.value)
    '''if isParent(pt,n1) and isParent(pt,n2):
        if pt.deep>lowest[1]:
            #print('%d,%d' % (pt.deep,pt.value))
            lowest = (pt.value,pt.deep)
    if pt.left is not None:
        find_lowest(n1,n2,pt.left,lowest)
    if pt.right is not None:
        find_lowest(n1,n2,pt.right,lowest)
    if pt.left is  None and pt.right is  None:
        return'''
    
    
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.strip().split()
    find_lowest(int(L[0]),int(L[1]),node,(30,0))

test_cases.close()
    

