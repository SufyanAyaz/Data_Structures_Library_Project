from myLib.datastructures.Trees.BST import BST
from myLib.datastructures.nodes.TNode import TNode



# BST default constructor test
BSTdefault = BST()
assert BSTdefault.getRoot() == None

# BST int overload constructor
BSTint = BST(2)
assert BSTint.getRoot().getData() == 2

# BST overlaod with no children test
BSTtnode = BST(TNode(2))
assert BSTtnode.getRoot().getData() == 2

# BST overlaod with children
TNodeWithChildren = TNode(1,0,TNode(0),TNode(4),TNode(5))
BSTwithChildren = BST(TNodeWithChildren)
assert BSTwithChildren.getRoot().getData() == 1
assert BSTwithChildren.getRoot().getBalance() == 0
assert BSTwithChildren.getRoot().getParent().getData() == 0
assert BSTwithChildren.getRoot().getLeft().getData() == 4
assert BSTwithChildren.getRoot().getRight().getData() == 5



# Test the BST insert
bst = BST()
bst.insert(10)
bst.insert(12)
bst.insert(4)
bst.insert(19)
bst.insert(16)
bst.insert(9)

assert bst.getRoot().getData() == 10
assert bst.getRoot().getLeft().getData() == 4
assert bst.getRoot().getLeft().getRight().getData() == 9   
assert bst.getRoot().getRight().getData() == 12
assert bst.getRoot().getRight().getRight().getData() == 19
assert bst.getRoot().getRight().getRight().getLeft().getData() == 16


# Test BST insert with TNode
bstTnode = BST(TNode(5))
bstTnode.insert(TNode(7))
bstTnode.insert(TNode(6))
bstTnode.insert(TNode(15))
bstTnode.insert(TNode(4))
assert bstTnode.getRoot().getData() == 5
assert bstTnode.getRoot().getLeft().getData() == 4
assert bstTnode.getRoot().getRight().getData() == 7
assert bstTnode.getRoot().getRight().getRight().getData() == 15
assert bstTnode.getRoot().getRight().getLeft().getData() == 6


# Test BST insert when BST is given a TNode value with children in the constructor
bstChild = BST(TNode(data=5, left=TNode(3), right=TNode(6)))
bstChild.insert(17)
bstChild.insert(2)
assert bstChild.getRoot().getData() == 5
assert bstChild.getRoot().getRight().getData() == 6
assert bstChild.getRoot().getLeft().getData() == 3
assert bstChild.getRoot().getLeft().getLeft().getData() == 2
assert bstChild.getRoot().getRight().getRight().getData() == 17



# Test the BST search
bstSearch = BST(TNode(5))
bstSearch.insert(TNode(7))
bstSearch.insert(TNode(6))
bstSearch.insert(TNode(15))
bstSearch.insert(4)
bstSearch.insert(19)
bstSearch.insert(16)

assert bstSearch.search(16).getData() == 16
assert bstSearch.search(5).getData() == 5
assert bstSearch.search(7).getData() == 7
assert bstSearch.search(19).getData() == 19
assert bstSearch.search(4).getData() == 4
assert bstSearch.search(6).getData() == 6
assert bstSearch.search(15).getData() == 15
assert bstSearch.search(100) == None
assert bstSearch.search(20) == None
assert bstSearch.search(45) == None
assert bstSearch.search(87) == None
assert bstSearch.search(8) == None



# Test BST delete

bstDel = BST()
bstDel.insert(10)
bstDel.insert(12)
bstDel.insert(4)
bstDel.insert(19)
bstDel.insert(16)
bstDel.insert(9)

print('Delete non existing node Test:')
bstDel.delete(100)
assert bstDel.getRoot().getData() == 10
bstDel.delete(10)
assert bstDel.getRoot().getData() == 9
bstDel.delete(9)
assert bstDel.getRoot().getData() == 4
bstDel.delete(4)
assert bstDel.getRoot().getData() == 12
bstDel.delete(12)
assert bstDel.getRoot().getData() == 19
bstDel.delete(19)
assert bstDel.getRoot().getData() == 16
bstDel.delete(16)
assert bstDel.getRoot() == None

# BST print in order test and print_bf test

bstPrint = BST(TNode(5))
bstPrint.insert(TNode(7))
bstPrint.insert(TNode(6))
bstPrint.insert(TNode(15))
bstPrint.insert(4)
bstPrint.insert(19)
bstPrint.insert(16)
print('Expected print in order result:')
print('4\n5\n6\n7\n15\n16\n19\n')
print('What the code retruns:')
bstPrint.print_in_order()
print()
print('Expected print bf results:')
print('5\n4 7\n6 15\n19\n16\n')
print('What the code retruns:')
bstPrint.print_bf()



# Test all parts of the BST
bstFinal = BST()
bstFinal.insert(50)
bstFinal.insert(25)
bstFinal.insert(75)
bstFinal.insert(10)
bstFinal.insert(30)
bstFinal.insert(60)
bstFinal.insert(80)
bstFinal.insert(5)

# Check if values were inserted correctly
assert bstFinal.search(50).getData() == 50
assert bstFinal.search(25).getData() == 25
assert bstFinal.search(75).getData() == 75
assert bstFinal.search(10).getData() == 10
assert bstFinal.search(30).getData() == 30
assert bstFinal.search(60).getData() == 60
assert bstFinal.search(80).getData() == 80
assert bstFinal.search(5).getData() == 5

# Delete some values
bstFinal.delete(30)
bstFinal.delete(60)

# Check if values were deleted correctly
assert bstFinal.search(30) == None
assert bstFinal.search(60) == None

# Add more values
bstFinal.insert(55)
bstFinal.insert(65)

# Check if values were added correctly
assert bstFinal.search(55).getData() == 55
assert bstFinal.search(65).getData() == 65

# Print tree using print_in_order() method
print('Expected print in order results:')
print('5\n10\n25\n50\n55\n65\n75\n80\n')
print('What the code returns:')
bstFinal.print_in_order()

# Print tree using print_bf() method
print('Expected print bf results:')
print('50\n25 75\n10 55 80\n5 65\n')
print('What the code returns:')
bstFinal.print_bf()