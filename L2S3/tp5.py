import list1,list2

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        p = self.head
        while p:
            yield p.data
            p = p.next    

    def add(self, data):
        node = Node(data)
        if self.head == None:   
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node                       
            self.head = node            

    def search(self, k):
        p = self.head
        if p!= None:
            while p.next != None:
                if (p.data==k):
                    return p                
                p = p.next
            if (p.data==k):
                return p
        return None

    def remove(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp        

    def __str__(self):
        s = ""
        p = self.head
        if p != None:      
            while p.next != None:
                s += p.data
                p = p.next
            s += p.data
        return ''.join(iter(self)) and s
### question 1
    
### question 2
def compare(a, b):
    """
    :param a: 
    :type a: any type 
    :param b:
    :type b: same as a
    :return:
       - -1 if a < b
       -  1 if a > b
       -  0 if a = b
    :UC: a and b must be comparable with <
    :Examples:

    >>> compare(0, 1)
    -1
    >>> compare('a', 'a')
    0
    >>> compare((2, 1), (1, 2))
    1
    """
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0
    
def is_sorted(linked_list, order):
    """
    documentation
    """
    iter1 = iter(linked_list)
    iter2 = iter(linked_list)
    next(iter2, None)
    if order=="normal":
        #if all(i1 <= i2 for i1, i2 in zip(iter1, iter2)):
        if all(compare(i1,i2)==-1 or compare(i1,i2)==0 for i1, i2 in zip(iter1,iter2)):
            return True
        else:
            return False
    if order=="reversed":
        #if all(i2 <= i1 for i1, i2 in zip(iter1, iter2)):
        if all(compare(i1,i2)==1 or compare(i1,i2)==0 for i1,i2 in zip(iter1,iter2)):
            return True
        else:
            return False
    return False

### question 3


def len_link(liste):
    temp=list2.head(liste)
    count=0
    while(temp):
        count+=1
        temp=temp.next
    return count


def msort3(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = msort3(x[:mid])
    z = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    return result




