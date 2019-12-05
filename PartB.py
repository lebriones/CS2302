
# Implementation of max heap
# Programmed by Olac Fuentes
# Last modified October 20, 2019

import matplotlib.pyplot as plt
import math


class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return -math.inf
        return self.tree[(i - 1) // 2]

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def insert(self, item):
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        if self.tree[parent_index] < self.tree[i]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()

        root = self.tree[0]
        self.tree[0] = self.tree.pop()

        self._percolate_down(0)

        return root

    def _percolate_down(self, i):

        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return

        max_child_index = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2

        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)


    def draw(self):
        if not self.is_empty():
            fig, ax = plt.subplots()
            self.draw_(0, 0, 0, 100, 50, ax)
            ax.axis('off')
            ax.set_aspect(1.0)

            plt.show()

    def draw_(self, i, x, y, dx, dy, ax):
        if self.left_child(i) > -math.inf:
            ax.plot([x, x - dx], [y, y - dy], linewidth=1, color='k')
            self.draw_(2 * i + 1, x - dx, y - dy, dx / 2, dy, ax)
        if self.right_child(i) > -math.inf:
            ax.plot([x, x + dx], [y, y - dy], linewidth=1, color='k')
            self.draw_(2 * i + 2, x + dx, y - dy, dx / 2, dy, ax)
        ax.text(x, y, str(self.tree[i]), size=20,
                ha="center", va="center",
                bbox=dict(facecolor='w', boxstyle="circle"))


def heap_sort(a_lst):
    h = MaxHeap()
    for a in a_lst:
        h.insert(a)
    i = len(a_lst) - 1
    while not h.is_empty():
        a_lst[i] = h.extract_max()
        i -= 1

def top_frequent_words(words, k):
    heap = MaxHeap()
    d = dict()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    
    for key in d:
        heap.insert(d[key])
    print(heap.tree)

def main():
    words = ["geeks", "for", "geeks", "a", 
                "portal", "to", "learn", "can",
                "be", "computer", "science", 
                 "zoom", "yup", "fire", "in", 
                 "be", "data", "geeks"]
    top_frequent_words(words, 1)


if __name__ == "__main__":
    main()
