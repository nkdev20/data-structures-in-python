class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class Tree:

    def __int__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, root):
        if data < root.data:
            if root.left != None:
                


if __name__ == "__main__":

