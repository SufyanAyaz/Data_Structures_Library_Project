from ..nodes.TNode import TNode
from ..Trees.BST import BST

class AVL(BST):
        
    def __init__(self, root=None):
        if isinstance(root, int):
            self.root = TNode(root)

        elif isinstance(root, TNode):
            if root.left is None or root.right is None:
                self.root = root
            else:
                self.root = root
                self.balance()
        else:
            self.root = None



    def setRootAVL(self, root):
        if isinstance(root, int):
            self.root = TNode(data=root)
        elif isinstance(root, TNode):
            if root.left is None and root.right is None:
                self.root = root
            else:
                self.root = root
                self.balance()
             
        else:
            self.root = None       

    def getRootAVL(self):
        return self.root
    

    def Insert(self, param):
        super().insert(param)
        self.balance()



    def balance(self):
        self.root = self.balanceWholeTree(self.root)



    def balanceFactor(self, node):
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        balance = left_height - right_height
        node.setBalance(balance)


    def rotateLeft(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root


    def rotateRight(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root


    def balanceWholeTree(self, node):
        if node is None: return None
        node.left = self.balanceWholeTree(node.left)
        node.right = self.balanceWholeTree(node.right)
        self.balanceFactor(node)
        balance_factor = node.getBalance()
        if balance_factor < -1:
            balance_factor_right = node.right.getBalance()
            if balance_factor_right > 0: node.right = self.rotateRight(node.right)
            node = self.rotateLeft(node)
        elif balance_factor > 1:
            balance_factor_left = node.left.getBalance()
            if balance_factor_left < 0: node.left = self.rotateLeft(node.left)
            node = self.rotateRight(node)
        return node
    
    def get_height(self, node):
        if node is None:
            return -1
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return max(left_height, right_height) + 1


    