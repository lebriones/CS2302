import os

BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'

class Node:
    def __init__(self, item=None, left=None, right=None, parent=None, color=None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color
        self.height = 1

class AVLTree:
    def __init__(self, root=None):
        self.root = root
        self.height = -1
        self.balance = 0
    
    def search(self, k):
        return self._search(k, self.root)
    
    def _search(self, k, Node):
        if Node is None:
            return False
        if Node.item == k:
            return True
        if k > Node.item:
            return self._search(k, Node.right)
        return self._search(k, Node.left)

    def __contains__(self, k):
        return self.search(k)
    
    def AVLTreeInsert(self, Node=None):
        if self.root is None:
            self.root = Node
            Node.parent = None
            return
        
        curr = self.root
        while curr is not None:
            if Node.item < curr.item:
                if curr.left is None:
                    curr.left = Node
                    Node.parent = curr
                    curr = None
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node
                    Node.parent = curr
                    curr = None
                else:
                    curr = curr.right
        Node = Node.parent
        while Node is not None:
            self.AVLTreeRebalance(Node)
            Node = Node.parent
    
    def AVLTreeRebalance(self, Node=None):
        self.AVLTreeUpdateHeight(Node)
        if self.AVLTreeGetBalance(Node) == -2:
            if self.AVLTreeGetBalance(Node.right) == 1:
                self.AVLTreeRotateRight(Node.right)
            return self.AVLTreeRotateLeft(Node)
        elif self.AVLTreeGetBalance(Node) == 2:
            if self.AVLTreeGetBalance(Node.left) == -1:
                self.AVLTreeRotateLeft(Node.left)
            return self.AVLTreeRotateRight(Node)
        return Node
    
    def AVLTreeRotateRight(self, Node=None):
        leftRightChild = Node.left.right
        if Node.parent is not None:
            self.AVLTreeReplaceChild(Node.parent, Node, Node.left)
        else:
            self.root = Node.left
            self.root.parent = None
        self.AVLTreeSetChild(Node.left, "right", Node)
        self.AVLTreeSetChild(Node, "left", leftRightChild)

    def AVLTreeRotateLeft(self, Node=None):
        rightLeftChild = Node.right.left
        if Node.parent is not None:
            self.AVLTreeReplaceChild(Node.parent, Node, Node.right)
        else:
            self.root = Node.right
            self.root.parent = None
        self.AVLTreeSetChild(Node.right, "left", Node)
        self.AVLTreeSetChild(Node, "right", rightLeftChild)
    
    def AVLTreeUpdateHeight(self, Node=None):
        leftHeight = -1
        if Node.left is not None:
            leftHeight = Node.left.height
        rightHeight = -1
        if Node.right is not None:
            rightHeight = Node.right.height
        Node.height = max(leftHeight, rightHeight) + 1
    
    def AVLTreeSetChild(self, parentN, whichChild, child):
        if whichChild != "left" and whichChild != "right":
            return False
        if whichChild == "left":
            parentN.left = child
        else:
            parentN.right = child
        if child is not None:
            child.parent = parentN
        self.AVLTreeUpdateHeight(parentN)
        return True
    
    def AVLTreeReplaceChild(self, parentN, currentChild, newChild):
        if parentN.left is currentChild:
            return self.AVLTreeSetChild(parentN, "left", newChild)
        elif parentN.right is currentChild:
            return self.AVLTreeSetChild(parentN, "right", newChild)
        return False
    
    def AVLTreeGetBalance(self, Node=None):
        leftHeight = -1
        if Node.left is not None:
            leftHeight = Node.left.height
        rightHeight = -1
        if Node.right is not None:
            rightHeight = Node.right.height
        return leftHeight - rightHeight
    
    def print_inorder(self):
        self._print_inorder(self.root)
    
    def _print_inorder(self, Node=None): 
        if Node is None: 
            return None
        # First recur on left child 
        self.print_inorder(Node.left) 
            # then print the data of node 
        print(Node.item)
            # now recur on right child 
        self.print_inorder(Node.right)  

class RBTree:
    def __init__(self, root=None):
        self.root = root
        self.height = -1
        self.balance = 0

    def search(self, k):
        return self._search(k, self.root)
    
    def _search(self, k, Node):
        if Node is None:
            return False
        if Node.item == k:
            return True
        if k > Node.item:
            return self._search(k, Node.right)
        return self._search(k, Node.left)

    def __contains__(self, k):
        return self.search(k)
    
    def print_inorder(self):
        self._print_inorder(self.root)
    
    def _print_inorder(self, node): 
        if node is None: 
            return
        # First recur on left child 
        self._print_inorder(node.left) 
            # then print the data of node 
        print(node.item)
            # now recur on right child 
        self._print_inorder(node.right) 
            
    
    def RBTreeInsert(self, Node=None):
        self.BSTreeInsert(Node)
        Node.color = RED
        self.RBTreeBalance(Node)

    
    def BSTreeInsert(self, Node=None):
        if self.root is None:
            self.root = Node
            Node.left = None
            Node.right = None
        else:
            curr = self.root
            while curr is not None:
                if Node.item < curr.item:
                    if curr.left is None:
                        curr.left = Node
                        curr = None
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node
                        curr = None
                    else:
                        curr = curr.right
            Node.left = None
            Node.right = None
    
    def RBTreeBalance(self, Node=None):
        if Node.parent is None:
            Node.color = BLACK
            return
        if Node.parent.color is BLACK:
            return
        parentA = Node.parent
        grandparentA = self.RBTreeGetGrandparent(Node)
        uncle = self.RBTreeGetUncle(Node)
        if uncle is not None and uncle.color == RED:
            parent.color = uncle.color = BLACK
            grandparent.color = RED
            RBTreeBalance(self, grandparentA)
            return
        if Node is parentA.right and parentA is grandparentA.left:
            self.RBTreeRotateLeft(parentA)
            Node = parentA
            parent = Node.parent
        elif Node is parent.left and parent is grandparentA.right:
            self.RBTreeRotateRight(parent)
            Node = parent
            parent = Node.parent
        parent.color = BLACK
        grandparent.color = RED
        if Node is parent.left:
            self.RBTreeRotateRight(grandparentA)
        else:
            self.RBTreeRotateLeft(grandparentA)
    
    def RBTreeGetGrandparent(self, Node=None):
        if Node.parent is None:
            return None
        return Node.parent.parent
    
    def RBTreeGetUncle(self, Node=None):
        grandparent = None
        if Node.parent is not None:
            grandparent = Node.parent.parent
        if grandparent is None:
            return None
        if grandparent.left is Node.parent:
            return grandparent.right
        else:
            return grandparent.left

    def RBTreeRotateLeft(self, Node=None):
        right_left_child = Node.right.left
        if Node.parent is not None:
            self.RBTreeReplaceChild(Node.parent, Node, Node.right)
        else:
            self.root = Node.right
            self.root.parent = None
        self.RBTreeSetChild(Node.right, "left", Node)
        self.RBTreeSetChild(Node, "right", right_left_child)
    
    def RBTreeRotateRight(self, Node=None):
        left_right_child = Node.left.right
        if Node.parent is not None:
            self.RBTreeReplaceChild(Node.parent, Node, Node.left)
        else:
            self.root = Node.right
            self.root.parent = None
        self.RBTreeSetChild(Node.left, "right", Node)
        self.RBTreeSetChild(Node, "left", left_right_child)

    def RBTreeSetChild(self, parentN, whichChild, child):
        if whichChild is not "left" and whichChild is not "right":
            return False
        if whichChild == "left":
            parentN.left = child
        else:
            parentN.right = child
        if child is not None:
            child.parent = parentN
        return True
    
    def RBTreeReplaceChild(self, parentN, current_child, new_child):
        if parentN.left is current_child:
            return self.RBTreeSetChild(parentN, "left", new_child)
        elif parentN.right is current_child:
            return self.RBTreeSetChild(parentN, "right", new_child)
        return False

def print_anagrams(word, english_words, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        #if english_words.search(str):
        if str in english_words:
           print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur

            if cur not in before: # Check if permutations of cur have not been generated.
                print_anagrams(before + after, english_words, prefix + cur)


def read_file(filename):
    x = input("AVL = 1, RB = 2\n")
    if x == '1':
        english_words = AVLTree()            
    elif x == '2':
        english_words = RBTree()
    else:
        print("Invalid choice")
    os.chdir(r'C:/Users/Luis/Desktop/Lab3')

    count = 0
    with open(filename) as f:
        for line in f:
            if x == '1':
                temp = Node(line.strip().lower())
                english_words.AVLTreeInsert(temp)
                #print(line)            
            if x == '2':
                temp = Node(line.strip().lower())
                english_words.RBTreeInsert(temp)

            count += 1

            if count % 1000 == 0:
                print("count: " , count)
                #print(line)
    #english_words.print_inorder()
    return english_words
       

def main():
    print_anagrams("spot", read_file("words.txt"))

if __name__=="__main__":
    main()