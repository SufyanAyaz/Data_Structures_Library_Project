from myLib.datastructures.Trees.BST import BST
from myLib.datastructures.nodes.TNode import TNode
from myLib.datastructures.Trees.AVL import AVL




# Test 1: Inserting left left case
print("\nAVL Test 1: Left Left case")
avl2 = AVL(10)
avl2.Insert(5)
avl2.Insert(3)
avl2.Insert(1)
avl2.Insert(7)
assert avl2.getRootAVL().getData() == 5
assert avl2.getRootAVL().getLeft().getData() == 3
assert avl2.getRootAVL().getRight().getData() == 10
assert avl2.getRootAVL().getLeft().getLeft().getData() == 1
assert avl2.getRootAVL().getRight().getLeft().getData() == 7
print('Expected Result:')
print('5\n3 10\n1 7\n')
avl2.print_bf()

# Test 2: Inserting right right case
print("\nAVL Test 2: Right Right case")
avl3 = AVL(10)
avl3.Insert(15)
avl3.Insert(17)
avl3.Insert(19)
avl3.Insert(13)

assert avl3.getRootAVL().getData() == 15
assert avl3.getRootAVL().getLeft().getData() == 10
assert avl3.getRootAVL().getRight().getData() == 17
assert avl3.getRootAVL().getLeft().getRight().getData() == 13
assert avl3.getRootAVL().getRight().getRight().getData() == 19

print('Expected Result:')
print('15\n10 17\n13 19\n')
print('Actual results')
avl3.print_bf()


# Test 3: Inserting left right case
print("\nAVL Test 3: Left Right case")
avl4 = AVL(10)
avl4.Insert(5)
avl4.Insert(8)
avl4.Insert(7)
avl4.Insert(9)
assert avl4.getRootAVL().getData() == 8
assert avl4.getRootAVL().getLeft().getData() == 5
assert avl4.getRootAVL().getRight().getData() == 10
assert avl4.getRootAVL().getLeft().getRight().getData() == 7
assert avl4.getRootAVL().getRight().getLeft().getData() == 9

print('Expected Result:')
print('8\n5 10\n7 9\n')
print('Actual results')
avl4.print_bf()

# Test 4: Inserting right left case
print("\nAVL Test 4: Right Left case")
avl5 = AVL(10)
avl5.Insert(15)
avl5.Insert(13)
avl5.Insert(14)
avl5.Insert(12)
assert avl5.getRootAVL().getData() == 13
assert avl5.getRootAVL().getLeft().getData() == 10
assert avl5.getRootAVL().getRight().getData() == 15
assert avl5.getRootAVL().getLeft().getRight().getData() == 12
assert avl5.getRootAVL().getRight().getLeft().getData() == 14


print('Expected Result:')
print('13\n10 15\n12 14\n')
print('Actual results')
avl5.print_bf()




# Create a BST and pass the root into the AVL class and see if if it balances
# Testing the constructors ability to balance
print("\nAVL Test 5: Constructor balance")
bstAvl = BST()
bstAvl.insert(10)
bstAvl.insert(12)
bstAvl.insert(4)
bstAvl.insert(19)
bstAvl.insert(16)
bstAvl.insert(9)
root = bstAvl.getRoot()
Avl = AVL(root)
assert Avl.getRootAVL().getData() == 10
assert Avl.getRootAVL().getRight().getData() == 16
assert Avl.getRootAVL().getLeft().getData() == 4
assert Avl.getRootAVL().getRight().getRight().getData() == 19
assert Avl.getRootAVL().getRight().getLeft().getData() == 12
assert Avl.getRootAVL().getLeft().getRight().getData() == 9

# print the tree in order
print('Expected Result:')
print('10\n4 16\n9 12 19\n')
print('Actual results')
Avl.print_bf()
print()


# same Test but for setRoot
print("\nAVL Test 6: setRoot balance")
bstAvlS = BST()
bstAvlS.insert(10)
bstAvlS.insert(12)
bstAvlS.insert(4)
bstAvlS.insert(19)
bstAvlS.insert(16)
bstAvlS.insert(9)

root = bstAvlS.getRoot()

AvlS = AVL()
AvlS.setRootAVL(root)

# print the tree in order
print('Expected Result:')
print('10\n4 16\n9 12 19\n')
print('Actual results')
AvlS.print_bf()


#default constructor test

AVLDefault = AVL()
assert AVLDefault.getRootAVL() == None

#overload int constructor
AVLint = AVL(5)
assert AVLint.getRootAVL().getData() == 5

#printlnOrder test
print("\nAVL Test 9: print order")
AVLOrder = AVL(8)
AVLOrder.Insert(1)
AVLOrder.Insert(543)
AVLOrder.Insert(90)
AVLOrder.Insert(13)

print('Expected Result:')
print('1\n8\n13\n90\n543\n')
print('Actual results')
AVLOrder.print_in_order()

