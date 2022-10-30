from dataclasses import dataclass
from re import S
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)
    size = 0                 # number of nodes
    s: str = " "


    def put(self, key, value):
        if key == self.key: # to replace the values
            self.value = value
        elif key < self.key: # we going left side 
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.put(key, value)
        else: # we going right side 
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.put(key, value)



    def to_string(self):
        # i need to keep digging in recursive calls till last/smallest
        # key and when i hit that condition, before close the call i need 
        # to print the value then go up in the calls
        # node = self 
        # once its None the call breaks and goes up

        if self.left is not None: 
            self.left.to_string()
        self.s += "(" + self.key + "," + str(self.value) + ")"
        # print(s)
        if self.right is not None:
            self.right.to_string()
        
        return self.s
    
        


    def count(self):
        # since it sat size to zero evertime
        # i used it as a incrment
        # i sat self.size = 1 !!
        self.size = 1
        if self.left is not None:
            self.size += self.left.count()
        if self.right is not None:
            self.size += self.right.count()
        
        return self.size

    def get(self, key):
        if self.key == key:
            return self.value
        elif key < self.key:
            if self.left is not None:
                return self.left.get(key)
            else:
                return None
        elif key > self.key:
            if self.right is not None:
                return self.right.get(key)
            else:
                return None
        

    def max_depth(self):
        left_side = 0
        right_side = 0
        # reach the bottom 
        if self.left is not None:
            left_side = self.left.max_depth()
        if self.right is not None:
            right_side = self.right.max_depth()

        # count going up the recursive call 
        if left_side > right_side:
            return left_side + 1
        else:
            return right_side + 1
        

    def count_leafs(self):
        leafs = 0
        if self.left is None and self.right is None:
            leafs += 1
        if self.left:  # dig left
            leafs += self.left.count_leafs()
        if self.right: # dig right
            leafs += self.right.count_leafs()

        return leafs

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        if self.left is not None:
            self.left.as_list(lst)
        lst.append((self.key, self.value))
        if self.right is not None:
            self.right.as_list(lst)
        
        return lst    # Placeholder code to avoid crash in demo program. To be replaced


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a leaf node count. That is, the number of nodes 
    # with no children
    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
