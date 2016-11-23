class BinaryTreeNode(object):
	"""A binary tree node, and in the recursive sense a nonempty binary tree. Each node in the binary tree has a stored value, a left child, and a right child."""
	
	def __init__(self, value=None):
		"""Initializes a new binary tree node with the given value (default None) and no children."""
		self.value = value
		self.left = None
		self.right = None
	
	def setValue(self, value):
		"""Stores the given object as the node's value."""
		self.value = value
	
	def getValue(self):
		"""Returns the value stored in the node."""
		return self.value
	
	def setLeftChild(self, binaryTreeNode):
		"""Sets the left child to the given BinaryTreeNode."""
		self.left = binaryTreeNode
	
	def getLeftChild(self):
		"""Returns the left child."""
		return self.left
	
	def setRightChild(self, binaryTreeNode):
		"""Sets the right child to the given BinaryTreeNode."""
		self.right = binaryTreeNode
	
	def getRightChild(self):
		"""Returns the right child."""
		return self.right
	
	def getHeight(self):
		"""Returns the height of the tree descending from this node. For example, if the node has no children then returns 0."""
		# Compute the height of the left subtree.
		if self.left == None:
			leftHeight = -1
		else:
			leftHeight = self.left.getHeight()
		# Compute the height of the right subtree.
		if self.right == None:
			rightHeight = -1
		else:
			rightHeight = self.right.getHeight()
		return 1 + max(leftHeight, rightHeight)
	
	def __str__(self):
		"""Returns a string representation, with an empty child represented by []. Assumes that the values stored in the tree themselves respond to __str__."""
		# Get the string for the left child.
		if self.left == None:
			leftString = '[]'
		else:
			leftString = str(self.left)
		# Get the string for the right child.
		if self.right == None:
			rightString = '[]'
		else:
			rightString = str(self.right)
		return '[' + str(self.value) + ', ' + leftString + ', ' + rightString + ']'

if __name__ == "__main__":
	myTree = BinaryTreeNode(17)
	myTree.setLeftChild(BinaryTreeNode('jan'))
	myTree.getLeftChild().setRightChild(BinaryTreeNode('juan'))
	myTree.setRightChild(BinaryTreeNode([3, 4, 5]))
	print ("The height is", myTree.getHeight())
	print (myTree)


class HuffmanTreeNode(BinaryTreeNode):
	"""A subclass of BinaryTreeNode. Acts in exact same manner as BTN except has an extra instance variable, weight, which stores the frequency of the instance variable value. Interior nodes' weight is the sum of all of its children. Nodes DO NOT KNOW THEIR OWN CODE! This is instead dealt with by another class, HuffmanTree, which contains a pointer to the root node and deals with the codewords."""

	def __init__(self, weight=0, value=None):
		"""Initializes a new Huffman tree node with given weight and value (though interior nodes will have value None) """
		BinaryTreeNode.__init__(self,value)
		self.weight = weight
		
	def setWeight(self, newWeight):
		"""Sets this node's weight to newWeight. Useful for interior nodes."""
		self.weight = newWeight
		
	def getWeight(self):
		"""Returns this node's weight """
		return self.weight
		
	def setLeftChild(self, node):
		"""Sets left child to given node, which will presumably be a HTN."""
		BinaryTreeNode.setLeftChild(self, node)
		self.weight += node.getWeight()
	
	def setRightChild(self, node):
		"""Sets right child to given node, which will presumably be a HTN."""
		BinaryTreeNode.setRightChild(self, node)
		self.weight += node.getWeight()
		
	def __str__(self):
		"""Returns a string representation - empty child is []. Easier to rewrite this method than to call it from superclass and alter it then."""
		if self.left == None:
			leftStr = '[]'
		else:
			leftStr = str(self.left)
			
		if self.right == None:
			rightStr = '[]'
		else: 
			rightStr = str(self.right)
			
		if self.value == None:
			valStr = 'None'
		else:
			valStr = str(self.value)
		return '[(' + valStr + ', ' + str(self.weight) + '),' + leftStr + ', ' + rightStr + ']'
		
if __name__ == "__main__":
	n = HuffmanTreeNode(12, 'a')
	m = HuffmanTreeNode(13, 'd')
	parent = HuffmanTreeNode()
	parent.setLeftChild(n)
	parent.setRightChild(m)
	print ('m: ' , m)
	print ('n: ' , n)
	print ('parent:', parent)
