import math

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return repr(self.data)

def LinkedList:
    def __init__(self):
        self._root = None
        self._data = {}
        
    def append(self, datum):
        self.data[datum] = None
        if self.root is None:
            self.root = Node(datum)
        else:
            cur = self.root
            while cur.next:
                cur = cur.next
            cur.next = Node(datum)

    def find(self, datum):
        if datum in self.data:
            cur = self.root
            index = 0
            while cur:
                if cur.data == datum:
                    return index
                index += 1
                cur = cur.next
        else:
            return -1
        
    def remove(self, datum):
        if datum not in self.data:
            return None
        else:
            self.data.pop(datum)
            root = self.root
            cur = self.root.next
            if root.data == datum:
                root.next = None
                self.root = cur
            else:
                prev = root
            while cur:
                if cur.data == datum:
                    prev.next = cur.next
                    cur = None
                    break
                prev = prev.next
                cur = cur.next

class HashTable:
    """
    Can only append data of type:
    * int
    * str
    * float
    """
    def __init__(self, array_size=100):
        self._array = [LinkedList()
                       for _ in range(array_size)]
        self.array_size = array_size
        
    def hash_function(self, x):
        if isinstance(x, int):
            return x
        if isinstance(x, float):
            return math.floor(x)
        if isinstance(x, str):
            ordinals = [ord(elem) for elem in x]
            return sum(ordinals)

    def get_index(self, datum):
        return self.hash_function(datum) % self.array_size
    
    def append(self, datum):
        index = self.get_index(datum)
        self._array[index].append(datum)
        

