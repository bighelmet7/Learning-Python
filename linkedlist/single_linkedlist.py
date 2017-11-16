#!/usr/bin/python3

#Classic Node implementation
class Node:
    """Very basic node exemple"""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value)
"""
should be implemented
class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
"""
def main():
    student = Node("s1")
    teacher = Node("t1", student)
    print(teacher)

if __name__ == '__main__':
    main()