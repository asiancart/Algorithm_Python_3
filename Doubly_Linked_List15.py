import sys

class Node:
    data = ""
    prev =None
    next =None

    def __init__(self,data):
        self.data = data

class LinkedList:
    _head = None
    _tail = None

    def init(self):
        self._head = Node("San Francisco")
        self._head.prev = None
        self._head.next = None

        node_oakland = Node("Oakland")
        node_oakland.prev = self._head
        node_oakland.next = None
        self._head.next = node_oakland
        node_berkeley = Node("Berkeley")
        node_berkeley.prev = node_oakland
        node_berkeley.next = None
        node_oakland.next =node_berkeley
        self._tail = Node("Fremont")
        self._tail.prev = node_berkeley
        self._tail.next = None
        node_berkeley.next = self._tail
        return self._head

    def output(self,node):
        p = node
        end = None
        while p!=None:
            print(p.data,"->",end="")
            end = p
            p = p.next
            print("End\n")

            p = end
            while p!= None:
                print(p.data,"->",end="")
                p = p.prev
                print("Start\n\n")


def main():
    linkedlist = LinkedList()
    head = linkedlist.init()
    linkedlist.output(head)


if __name__ == "__main__":
    main()