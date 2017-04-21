#!/usr/bin/python

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.value = key
        self.left = left
        self.right = right

    def getKey(self):
        return self.key

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left
        
    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def __insert(self,current, data):
        newNode = Node(data)
        if current is None:
            return newNode
        elif data < current.getKey():
            current.setLeft(self.__insert(current.getLeft(), data))
        elif data > root.getKey():
            current.setRight(self.__insert(current.getRight(), data))
        return current

    def insert(self, data):
        self.root = self.__insert(self.root, data)
        
    #def delete(self, data):

    def search(self, data):
        found = False
        current = self.root
        while current and found == False:
            if data == current.getKey():
                found = True
            elif data < current.getKey():
                current = current.getLeft()
            else:
                current = current.getRight()
        return found

myTree = BinarySearchTree()
myTree.insert(5)
myTree.insert(3)
myTree.insert(1)
print myTree.search(1)

