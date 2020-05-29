class Node():
    def __init__(self, data=None):
        self.data, self.left, self.right = data, None, None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def _insert_rec(self, data, node):
        if node.data == data:
            #Not allowing duplicates right now
            return
        elif data > node.data:
            if node.right:
                return self._insert_rec(data, node.right)
            else:
                node.right = Node(data)
                return
        else:
            if node.left:
                return self._insert_rec(data, node.left)
            else:
                node.left = Node(data)
                return

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        else:
            self._insert_rec(data, self.root)
            return
    
    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        print(node.data)
        self.inOrder(node.right)

    def preOrder(self, node):
        if not node:
            return
        print(node.data)
        self.inOrder(node.left)
        self.inOrder(node.right)

    def postOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        self.inOrder(node.right)
        print(node.data)

if __name__=='__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(5)
    bst.insert(100)
    bst.insert(1)
    bst.insert(2)
    bst.insert(15)
    bst.inOrder(bst.root)
