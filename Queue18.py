#First in first out

import sys
class Node:
    data = ""
    next = None
    prev = None

    def __init__(self,data):
        self.data = data

class Queue:
    _head = None
    _tail = None
    _size = 0

    def offer(self,element):
        if self._head == None:
            self._head = Node(element)
            self._tail = self._head
        else:
            new_node = Node(element)
            new_node.next = self._tail
            self._tail.prev = new_node
            self._tail = new_node
            self._size +=1

    def poll(self):
        p = self._head
        if p == None:
            return None
        self._head = self._head.prev
        p.next = None
        p.prev = None
        self._size -=1
        return p

    def size(self):
        return self._size

    def output(self,queue):
        print("Head",end="")
        node = queue.poll()
        while node != None:
            print(node.data,"<-",end="")
            node = queue.poll()
            print("Tail\n")


def main():
    queue = Queue()
    queue.offer("A")
    queue.offer("B")
    queue.offer("C")
    queue.offer("D")
    queue.output(queue)

if __name__ == "__main__":
    main()