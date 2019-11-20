class Node:
    def __init__(self, item=None, next=None, prev=None):
        self.item = item
        self.key = key
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, head=None, tail = None):
        self.head = head
        self.tail = tail
    
    def add_node(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None
    
    def print_list(self):
        curr = self.head

        while curr is not None:
            print(curr.item, end=' ')
            curr = curr.next
    
    def delete_node(self, val):
        if self.head.item is val:
            self.head = self.head.next
            self.head.prev = None
            return self.head
        elif self.tail.item is val:
            self.tail = self.tail.prev
            self.tail.next = None
            return self.tail
        else:
            curr = self.head.next
            while curr.next is not None:
                if curr.item == val:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    return curr
                else:
                    curr = curr.next
        return None
    

class LRU:
    def __init__(self, capacity):
        self.cache = dict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        return self.cache[key].item
    
    def put(self, key, value):
        if key in self.cache:
            node = self.hash_map[key]
            node.value = value

        else:
            new_node = Node(key, value)
            if self.size() == self.capacity:
                self.remove(self.end)
            self.add_node(new_node)
            self.cache[key] = new_node
    
    def size(self):
        return len(self.cache)
  
    def max_capacity(self):
        return self.capacity

def main():
    L1 = LRU(4)
    L1.put(0, 10)
    L1.put(1, 20)
    L1.put(2, 30)
    L1.put(3, 40)
    L1.put(4, 50)


if __name__ == "__main__":
    main()
    
    

         