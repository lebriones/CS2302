import os

class Node:
    def __init__(self, item=None, next=None, password=None, count=0):
        self.item = item
        self.next = next
        #self.password = password
        self.count = count


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_last(self, item):

        if self.head is None:  # If the list is empty, add a new head
            self.head = Node(item, self.head)
            return

        curr = self.head
        while curr.next is not None:  # Looking for the second to last node
            curr = curr.next

        curr.next = Node(item)

    def add_first(self, item):
        self.head = Node(item, self.head)

    def add(self, index, item):
        if index == 0:
            self.head = Node(item, self.head)
            return

        if index < 0:  # Don't do anything if index is invalid
            return

        curr = self.head
        for i in range(index - 1):  # Looking for the node at position index - 1
            if curr is None:
                return

            curr = curr.next

        if curr is not None:
            curr.next = Node(item, curr.next)

    def clear(self):
        self.head = None

    def contains(self, item):
        return self.index_of(item) != -1

    def index_of(self, item):
        curr = self.head
        i = 0
        while curr is not None:
            if curr.item == item:
                return i
            i += 1
            curr = curr.next
        return -1

    def get(self, index):
        if index < 0:
            return None

        curr = self.head

        for i in range(index):  # Looking for node at position index. If no such element exists, return None
            if curr is None:
                return None

            curr = curr.next

        return None if curr is None else curr

    def get_first(self):
        return None if self.head is None else self.head.item

    def get_last(self):
        if self.head is None:
            return None

        curr = self.head
        while curr.next is not None:  # Looking for the last node in the list
            curr = curr.next

        return curr.item

    def remove(self, index):
        if index < 0:  # Don't do anything if index is invalid
            return

        if index == 0:  # Handling special case - when the item to remove is the head
            self.remove_first()
            return

        curr = self.head

        for i in range(index - 1):  # Looking for the second to last node
            if curr is None:
                return

            curr = curr.next

        if curr is not None and curr.next is not None:
            curr.next = curr.next.next

    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next

    def remove_last(self):
        if self.head is None or self.head.next is None:  # Handling special cases - empty or 1-element list
            self.head = None
            return

        # The list has at least two elements if this line is reached
        curr = self.head

        while curr.next.next is not None:
            curr = curr.next

        curr.next = None

    def size(self):
        curr = self.head

        length = 0
        while curr is not None:
            length += 1
            curr = curr.next

        return length

    def is_empty(self):
        return self.head is None

    def print_list(self):
        curr = self.head

        while curr is not None:
            print("Password:", curr.item, "\nCount:", curr.count)
            print()
            curr = curr.next

def read_file(filename):
    ll = SinglyLinkedList()
    d = dict()
    os.chdir(r'C:/Users/Luis/Desktop/CS2302/Lab2')
    with open(filename) as f:
        for line in f:
            curLine = line.split()
            password = curLine[0]
            print(password)
            
            #Checks and adds to dictionary
            if password in d:
                d[password] += 1
            else:
                d[password] = 1

            #Checks and adds to linked list
            if ll.contains(password):
                ll.get(ll.index_of(password)).count += 1
            else:
                ll.add_last(password)
                ll.get(ll.index_of(password)).count += 1
    ll.print_list()
    for pw in d:
        print(pw, d[pw])


def main():
    read_file("passwords2.txt")


if __name__ == "__main__":
    main()