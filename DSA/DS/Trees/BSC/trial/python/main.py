class Node:
    def __init__(self, data):
        self.left = None;
        self.right = None;
        self.data = data;

class Tree:
    def __init__(self):
        self.root = None;

    def createNode(self, data):
        return Node(data);

    def insert(self, data):
        if not self.root:
            self.root = createNote(data);
            return;
        if data < 
