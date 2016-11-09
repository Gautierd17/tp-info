class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, x):
        self.length+=1
        if self.first == None:
            #self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            #здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)

L = LinkedList()
L.add(1)
L.add(2)
L.add(3)
print(L)            
