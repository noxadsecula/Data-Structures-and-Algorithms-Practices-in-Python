class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.BSTInsert(self.root, new_val)
        
    
    def BSTInsert(self, node , new_val):
        if node.value == None:
            node.value = new_val
            return

        if node.value == new_val:
            return print('Value is already in the tree')

        if new_val < node.value:
            if node.left:
                node.left = BST(new_val)
            return

        if node.right:
            node.right = BST(new_val)
        return

        



    def search(self, find_val):
        return self.BSTSearch(self.root,find_val)

    def BSTSearch(self, node , find_val):
        if find_val == node.value:
            return True
        if find_val < node.value:
            if node.left == None:
                return self.BSTSearch(node.left,find_val)
        if node.right == None:
            return False
        return self.BSTSearch(node.right,find_val)
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))