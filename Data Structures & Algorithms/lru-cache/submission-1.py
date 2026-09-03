class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right
    
    #remove from the list
    def remove(self, node):
        nxt = node.next
        prv = node.prev
        prv.next = nxt
        nxt.prev = prv

    #insert at rightmost position right before our right pointer
    def insert(self, node):
        prv = self.right.prev
        node.prev = prv
        node.next = self.right
        self.right.prev = node
        prv.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        tempnode = Node(key, value)
        self.cache[key] = tempnode
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del(self.cache[lru.key])



        
