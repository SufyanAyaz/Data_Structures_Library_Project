from myLib.datastructures.nodes.TNode import TNode

# Test the TNode default constructor 
TNodeDefault = TNode()
assert TNodeDefault.getData() == 0
assert TNodeDefault.getLeft() == None
assert TNodeDefault.getRight() == None
assert TNodeDefault.getParent() == None
assert TNodeDefault.getBalance() == 0

# Test the TNode constructor with only a data value
TNodeOneVal = TNode(3)
assert TNodeOneVal.getData() == 3
assert TNodeOneVal.getBalance() == 0
assert TNodeOneVal.getLeft() == None
assert TNodeOneVal.getRight() == None
assert TNodeOneVal.getParent() == None

# Test the TNode overload constructor
parent = TNode(2)
left = TNode(3)
right = TNode(4)
TNodeOverload = TNode(5,1,parent, left, right)
assert TNodeOverload.getData() == 5
assert TNodeOverload.getBalance() == 1
assert TNodeOverload.getLeft() == left
assert TNodeOverload.getRight() == right
assert TNodeOverload.getParent() == parent


# TNode setter test
setDataTest = TNode(7)
assert setDataTest.getData() == 7
setDataTest.setData(4)
assert setDataTest.getData() == 4


# TNode getter test
getDataTest = TNode(15)
assert getDataTest.getData() == 15


# TNode toString test
toStringTest = TNode(20)
dataString = toStringTest.toString()
assert dataString == '20'

# Tnode print_node test 
print('Testing TNode Print:')
printTNode = TNode(30)
print('Expected\nNode data: 30 \nNode balance: 0\n')
print('Actual')
printTNode.print_node()
print()
