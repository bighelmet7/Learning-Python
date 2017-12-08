#!/usr/bin/python

class Node:
    """
    Implementation of a node
    """
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        if self.value:
            print("Node information, value: %s" % str(self.value))
        else:
            print("Empty Node")

class Tree:
    """
    Implementation of a tree
    """
    def __init__(self, root):
        if root.__class__ is Node:
            self.root = root
    
    def height_tree(self, p):
        """
        Returns the height of the tree pointed by p, if its a empty
        tree returns -1
        """
        if p:
            left = right = 0
            if p.left:
                left = self.height_tree(p.left) + 1
            if p.right:
                right = self.height_tree(p.right) + 1
            return max(left, right)
        else:
            return -1
    
    def find_node(self, p, value):
        """
        find_node returns true if p is in the tree, otherwise false
        """
        if p:
            if value > p.value:
                return self.find_node(p.right, value)
            if value < p.value:
                return self.find_node(p.left, value)
            return True
        return False

    def insert_value(self, p, v):
        """
        inser_node insert the v value in the tree pointed by p
        """
        if p:
            if v < p.value:
                if not p.left:
                    p.left = Node(v, None, None)
                self.insert_value(p.left, v)
            elif v > p.value:
                if not p.right:
                    p.right = Node(v, None, None)
                self.insert_value(p.right, v)
            else:
                p.value = v
        else:
            self.root = Node(v, None, None)
    
    def min_node(self, p):
        """
        Returns the minimum node value of the tree pointed by p
        """
        while(p.left): p = p.left
        return p.value

    def max_node(self, p):
        """
        Returns the maximum node value of the tree pointed by p
        """
        while(p.right): p = p.right
        return p.value
    
    def delete_node(self, p):
        """
        TODO: UNDERSTAND HOW TO IMPLEMENTED
        """
        pass

    """
    This OK but use the BST definition
    def min_node(self, p):
        #returns the minum node in the tree pointed by p
        if p:
            min_left = min_right = p.value
            if p.left:
                min_left = self.min_node(p.left)
            if p.right:
                min_right = self.min_node(p.right)
            return min(p.value, min(min_left, min_right))
    """
    """
    This is fine but use the BST definition...
    def max_node(self, p):
        #returns the maximum node in the tree pointed by p
        if p:
            max_left = max_right = p.value
            if p.left:
                max_left = self.max_node(p.left)
            if p.right:
                max_right = self.max_node(p.right)
            return max(p.value, max(max_left, max_right))
    """
    def print_tree(self, p):
        """
        print_tree prints the tree pointed by p, with the next logics:
                 10
               /    \
              3      11
            /   \    / \
           1     4  0   0
          / \   / \
        0    0 0   0
        Every leaf, is represented by two follewed 0's
        """
        if p:
            print(p.value)
            if p.left:
                self.print_tree(p.left)
            if not p.left:
                print("0")
            if p.right:
                self.print_tree(p.right)
            if not p.right:
                print("0")

def main():
    """
    Exemple to implement BST in python
    """
    n11 = Node(1, None, None)
    n12 = Node(4, None, None)
    n1 = Node(3, n11, n12)
    n2 = Node(13, None, None)
    root = Node(11, n1, n2)
    t = Tree(root)
    print("The height of the tree is: ", t.height_tree(t.root))
    print("Is 5 in the tree? ", t.find_node(t.root, 5))
    #print(t.print_tree(t.root))
    t.insert_value(t.root, 12)
    print(t.print_tree(t.root))
    print("The minimum value node is: ", t.min_node(t.root))
    print("The maximum value node is: ", t.max_node(t.root))


if __name__ == '__main__': main()