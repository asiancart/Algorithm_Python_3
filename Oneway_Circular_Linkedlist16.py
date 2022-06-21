import sys

class Node:
    data = ""
    next = None

    def __init__(self,data):
        self.data = data


class LinkedList:
    _head = None
    _tail = None

    def init(self):
        self._head = Node("A")
        self._head.next = None
        nodeB = Node("B")
        nodeB.next = None
        self._head.next = nodeB

        nodeC= Node("C")
        nodeC.next = None
        nodeB.next = nodeC

        self._tail = Node("D")
        self._tail.next = self._head
        nodeC.next = self._tail

    def output(self):
        p = self._head
        print(p.data,"->",end="")
        p = p.next
        while p != self._head:
            print(p.data, "->",end="")
            p=p.next
            print(p.data,"\n\n")


def main():
    linkedlist = LinkedList()
    linkedlist.init()
    linkedlist.output()


if __name__ == "__main__":
    main()