class LinkedListNode(object):
	"""A basic linked list node class, for use in implementing other more interesting classes."""
	
	def __init__(self, data):
		"""Initializes a new node with the given data and no next node."""
		self.data = data
		self.next = None
	
	def setData(self, data):
		"""Sets the node's data, which is set for the first time in __init__()."""
		self.data = data
	
	def getData(self):
		"""Returns the data currently stored in the node."""
		return self.data
	
	def setNext(self, next):
		"""Sets the next node, which is None by default."""
		self.next = next
	
	def getNext(self):
		"""Returns the next node, or None."""
		return self.next
	
	def __str__(self):
		"""Returns data as string"""
		return self.data

if __name__ == "__main__":
	node = LinkedListNode('hello')
	node2 = LinkedListNode('bye')
	node3 = LinkedListNode('later')
	node.setNext(node2)
	node2.setNext(node3)
	
	temp = node
	while temp != None:
		print str(temp)
		temp = temp.getNext()

class Queue(object):
    def __init__(self):
        """Initializes an empty queue."""
	self.front = None
	self.back = None
	self.count = 0
	
    def enqueue(self, x):
	"""Puts the given object into the queue, at the back."""
	if self.count == 0:
		self.front = LinkedListNode(x)
		self.back = self.front
	else:
		temp = LinkedListNode(x)
		self.back.setNext(temp)
		self.back = temp
		self.count += 1
	
	def dequeue(self):
		"""If the queue is not empty, then removes the front object and returns it. If the queue is empty, then does nothing and returns None."""
		if self.count == 0:
			return None
		else:
			temp = self.front.getData()
			self.front = self.front.getNext()
			if self.count == 1:
				self.back = None
			self.count -= 1
			return temp
	
	def peek(self):
		"""If the queue is not empty, then returns the front object, without removing it from the queue. If the queue is empty, then returns None."""
		if self.front == None:
			return None
		else:
			return self.front.getData()
	
	def __len__(self):
		"""Returns the number of objects in the queue."""
		return self.count
	
	def __str__(self):
		"""Returns a human-readable string representation of the queue, from front to back, assuming that the objects in the queue themselves respond to the __str__ method."""
		if self.count == 0:
			return "()"
		elif self.count == 1:
			return "(" + str(self.front.getData()) + ")"
		else:
			# There are at least two objects; commas are needed.
			string = "(" + str(self.front.getData())
			current = self.front.getNext()
			while current != None:
				string += ", " + str(current.getData())
				current = current.getNext()
			string += ")"
			return string

# If this file was executed (rather than imported), then run this demo.
if __name__ == "__main__":
	myQueue = Queue()
	print myQueue
	myQueue.enqueue("Jill")
	print myQueue
	myQueue.enqueue("John")
	print myQueue
	print myQueue.getSize()
	print myQueue.dequeue()
	print myQueue
	myQueue.enqueue(2.0 * 3.14159)
	print myQueue
	myQueue.enqueue("Jenny")
	print myQueue
	print myQueue.dequeue()
	print myQueue
	print myQueue.dequeue()
	print myQueue
	print myQueue.dequeue()
	print myQueue
	print myQueue.dequeue()
	print myQueue
	
