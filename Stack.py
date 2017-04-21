#! /usr/bin/python

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def delete(self, data):
        current = self.head
        previous = current
        while current:
            if current.getData() == data:
               previous.setNext(current.getNext())
               current.setNext(None)
            else:
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError("Data not in linked list")
    
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        if current is None:
            raise ValueError("Data not in linked list")
        return current

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count

myList = LinkedList()
ans = True
while ans:
    print("""
    1. Insert
    2. Delete
    3. Search
    4. Size
    5. Exit
    """)
    ans = raw_input("Please Select: ")
    if ans == '1':
        data = raw_input("Enter data to insert: ")
        myList.insert(data)
    elif ans == '4':
        print "Size of list is " + str(myList.size())
    elif ans == '5':
        ans = False

print myList.size()
