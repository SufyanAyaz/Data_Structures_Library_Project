class TNode:
    def __init__(self, data=0, balance=0,parent=None, left=None, right=None):
        if isinstance(data, int):
            self.data=data
        else:
            self.data = None
        if isinstance(balance, int):
            self.balance=balance
        else:
            self.balance = None
        if isinstance(parent, TNode):
            self.parent=parent
        else:
            self.parent = None

        if isinstance(left, TNode):
            self.left=left
        else:
            self.left = None

        if isinstance(right, TNode):
            self.right=right
        else:
            self.right = None
            

    def setData(self, data):
        self.data = data
    
    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self.right = right
    
    def setParent(self, parent):
        self.parent = parent
    
    def setBalance(self, balance):
        self.balance = balance



    def getData(self):
        return self.data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getParent(self):
        return self.parent
    
    def getBalance(self):
        return self.balance

    
    def print_node(self):
        print(f"Node data: {self.data}")
        print(f"Node balance: {self.balance}")

    def toString(self):
        return str(self.data)


