class Node:
    def __init__(self, value, key, next=None, prev=None):
        self.val = value
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity, head=None, tail=None):
        self.capacity = capacity
        self.dic = dict()
        self.head = head
        self.tail = tail
    
    #returns the value associated with the key and updates that key as the MRU
    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        return -1

    #inserts the given key with the given value, replaces if key already exists, inserts where necessary
    def put(self, key, value):
        if key in self.dic:
            self.remove_node(self.dic[key])
        node = Node(key, value)
        self.add_node(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            del self.dic[self.head.key]
            self.head = self.head.next

    def remove_node(self, node):
        if self.head is None and self.tail is None: #linked list is empty
            return None
        elif self.head == self.tail: #only one node in linked list
            self.head = None
            self.tail = None
        elif node == self.head:
          self.head = self.head.next  
        elif node == self.tail:
            self.tail = self.tail.prev
        else: #node is somewhere in the middle of the linked list
            previous_node = node.prev
            next_node = node.next
            previous_node.next = next_node
            next_node.prev = previous_node

    def add_node(self, node):
        if self.head is None:
            self.head = node
        if self.tail is None:
            self.tail = node
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.dic[node.key] = node
    
    def print_list(self):
        curr = self.head
        while curr is not None:
            print("Key:", curr.key, "Value:", curr.val) 
            curr = curr.next
    
    def print_map(self):
        for key in self.dic:
            print(self.dic[key].val)
    
    def size(self):
        return len(self.dic)
  
    def max_capacity(self):
        return self.capacity

def main():
    cache = LRUCache(7)
    cache.put(1, 10)
    cache.put(2, 20)
    print(cache.size())
    cache.print_list()
    cache.put(3, 30)
    print(cache.get(2))
    cache.put(4, 40)
    cache.print_list()
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
    print(cache.size())
    print(cache.max_capacity())
    

if __name__ == "__main__":
    main()
    
    

         
