from ..nodes.TNode import TNode
class BST:
    def __init__(self, val=None):
        self.root = None
        if isinstance(val, int):
            self.root = TNode(val)
        if isinstance(val, TNode):
            self.root = val


    def setRoot(self, root):
        self.root = root
    def getRoot(self):
        return self.root
    

    def insert(self, val):
        if isinstance(val, int):

            new_node = TNode(data=val)
            if self.search(new_node.getData()) is not None:
                return

            if self.root is None:
                self.root = new_node
                return
            current_node = self.root
            while current_node:
                if val < current_node.getData():
                    if current_node.getLeft() is None:
                        current_node.setLeft(new_node)
                        new_node.setParent(current_node)
                        return
                    current_node = current_node.getLeft()
                else:
                    if current_node.getRight() is None:
                        current_node.setRight(new_node)
                        new_node.setParent(current_node)
                        return
                    current_node = current_node.getRight()
        elif isinstance(val, TNode):
            if self.search(val.getData()) is not None:
                return

            if self.root is None:
                self.root = val
                return
            current_node = self.root
            while current_node:
                if val.getData() < current_node.getData():
                    if current_node.getLeft() is None:
                        current_node.setLeft(val)
                        val.setParent(current_node)
                        return
                    current_node = current_node.getLeft()
                else:
                    if current_node.getRight() is None:
                        current_node.setRight(val)
                        val.setParent(current_node)
                        return
                    current_node = current_node.getRight()



    def search(self, val):
        current_node = self.root
        while current_node is not None:
            if current_node.getData() == val:
                return current_node
            elif current_node.getData() < val:
                current_node = current_node.getRight()
            else:
                current_node = current_node.getLeft()
        return None

    def delete(self, val):
        node = self.search(val)
        if node is None:
            print(f"Value {val} not found in the tree")
            return

        if node.getLeft() is None and node.getRight() is None:
            if node.getParent() is None:
                self.root = None
            elif node.getParent().getLeft() == node:
                node.getParent().setLeft(None)
            else:
                node.getParent().setRight(None)

        elif node.getLeft() is None:
            child = node.getRight()
            if node.getParent() is None:
                self.root = child
            elif node.getParent().getLeft() == node:
                node.getParent().setLeft(child)
            else:
                node.getParent().setRight(child)
            child.setParent(node.getParent())

        elif node.getRight() is None:
            child = node.getLeft()
            if node.getParent() is None:
                self.root = child
            elif node.getParent().getLeft() == node:
                node.getParent().setLeft(child)
            else:
                node.getParent().setRight(child)
            child.setParent(node.getParent())

        else:
            pred = node.getLeft()
            while pred.getRight() is not None:
                pred = pred.getRight()

            node_data = node.getData()
            node.setData(pred.getData())
            pred.setData(node_data)

            if pred.getLeft() is None:
                if pred.getParent().getLeft() == pred:
                    pred.getParent().setLeft(None)
                else:
                    pred.getParent().setRight(None)
            else:
                if pred.getParent().getLeft() == pred:
                    pred.getParent().setLeft(pred.getLeft())
                else:
                    pred.getParent().setRight(pred.getLeft())
                pred.getLeft().setParent(pred.getParent())

        node.setParent(None)  


    def print_in_order(self):
        stack = []
        current = self.root
        done = False
        while not done:
            if current is not None:
                stack.append(current)
                current = current.getLeft()
            elif stack:
                current = stack.pop()
                print(current.getData())
                current = current.getRight()
            else:
                done = True



    def print_bf(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                print(node.getData(), end=" ")
                if node.getLeft() is not None:
                    queue.append(node.getLeft())
                if node.getRight() is not None: 
                    queue.append(node.getRight())
            print() 
    