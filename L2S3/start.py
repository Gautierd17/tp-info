class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		self.prev = None

class LinkedList :
	def __init__( self ) :
		self.head = None		

	def add( self, data ) :
		node = Node( data )
		if self.head == None :	
			self.head = node
		else :
			node.next = self.head
			node.next.prev = node						
			self.head = node			

	def search( self, k ) :
		p = self.head
		if p != None :
			while p.next != None :
				if ( p.data == k ) :
					return p				
				p = p.next
			if ( p.data == k ) :
				return p
		return None

	def remove( self, p ) :
		tmp = p.prev
		p.prev.next = p.next
		p.prev = tmp		

	def __str__( self ) :
		s = ""
		p = self.head
		if p != None :		
			while p.next != None :
				s += p.data
				p = p.next
			s += p.data
		
                        
		return( ','.join(s))
                

# example code
##l = LinkedList()
##
##l.add( 'a' )
##l.add( 'b' )
##l.add( 'c' )
##
##print (l)

def native2list(l):
    strlist = [str(x) for x in l]
    strlist.reverse() #reversing a list to save order of native list elements
    if len(strlist)!=0:
        li=LinkedList()
        for item in strlist:
            li.add(item)
        print(li)
    else:        
        return []

def list2native(l):
    linked_list = native2list(l)
##    for x in l:
##        return str(x if linked_list is None else linked_list)
