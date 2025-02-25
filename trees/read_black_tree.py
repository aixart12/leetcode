
# TODO -> not complete 
class RedBlackTree:
    class Node:
        def __init__(self , data):
            self.data = data
            self.left = None
            self.right = None
            self.colour = 'R'
            self.parent = None

    def __init__(self):
        self.root = None
        self.ll = False # Left-left Rotation flag
        self.rr = False # Right-Right Rotation flag
        self.lr = False # Left Right Rotaiton flag
        self.rl = False # Right-Left Rotation flag




    
        