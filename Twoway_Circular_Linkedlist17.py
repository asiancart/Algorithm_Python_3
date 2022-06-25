import sys

class Node:
    data =""
    next = None
    prev = None

    def __init__(self,data):
        self.data = data

class LinkedList:
    _head = None
    _tail = None

    def init(self):
        self._head = Node("A")
        self._head.next = None
        self._head.prev = None

        nodeB = Node("B")
        nodeB.next = None
        nodeB.prev = self._head
        self._head.next = nodeB

        nodeC = Node("C")
        nodeC.next = None
        nodeC.prev = nodeB
        nodeB.next = nodeC

        self._tail = Node("D")
        self._tail.next = self._head
        self._tail.prev = nodeC
        nodeC.next = self._tail
        self._head.prev = self._tail

    def output(self):
        p = self._head
        print(p.data,"->",end="")
        p = p.next
        while p !=self._head:
            print(p.data,"->",end="")
            p = p.next
            print(p.data,"\n\n",end="")
            p = self._tail
            print(p.data,"->",end="")
            p = p.prev
            while p != self._tail:
                print(p.data,"->",end="")
                p = p.prev
                print(p.data,"\n\n",end="")


def main():
    linkedlist = LinkedList()
    linkedlist.init()
    linkedlist.output()


if __name__ =="__main__":
    main()