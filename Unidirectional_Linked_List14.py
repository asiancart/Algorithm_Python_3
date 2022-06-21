import sys


class Node():
    data = ""
    next = None

    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    _head = None
    _tail = None

    def init(self):
        self._head = Node("San Francisco", None)
        node_oakland = Node("Oakland", None)
        self._head.next = node_oakland
        node_berkeley = Node("Berkeley", None)
        node_oakland.next = node_berkeley
        self._tail = Node("Fremont", None)
        node_berkeley.next = self._tail
        return self._head

    def output(self, node):
        p = node
        while (p != None):
            data = p.data
            print(data, "->", end="")
            p = p.next


def main():
    linkedlist = LinkedList()
    head = linkedlist.init()
    linkedlist.output(head)


if __name__ == "__main__":
    main()


"""
def insert(self,insert_position,new_bode):
    p = self._head
    i = 0
    while p.next != None and i < insert_position-1:
        p = p.next
        i +=1
    
    new_node.next = p.next
    p.next = new_node
    
    (main)linkedlist(2,Node("Walnut"),None)
"""


"""
def remove(self,remove_position):
    p = self._head
    i = 0
    
    while p.next != None and i<remove_position-1:
        p=p.next
        i +=1
        temp = p.next
        p.next = p.next.next
        temp.next = None
        
(main) linkedlist.remove(2)

"""