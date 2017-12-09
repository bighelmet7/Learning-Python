#!/usr/bin/python

class Heap:
    """
    Implementation of a min heap
    """
    def __init__(self):
        self.queue = [0]

    def _min_child(self, left_child, right_child):
        """
        Returns the min_child in the queue
        """
        if self.queue[left_child] > self.queue[right_child]:
            return right_child
        else:
            return left_child

    def _sort_heap(self):
        """
        Reestablish the heap order
        """
        i = 1
        n = len(self.queue)
        while 2 * i + 1 < n:
            pos_min_child = self._min_child(int(2 * i), int(2 * i + 1))
            if self.queue[i] > self.queue[pos_min_child]:
                #Change values
                aux = self.queue[pos_min_child]
                self.queue[pos_min_child] = self.queue[i]
                self.queue[i] = aux
            i += 1
                

    def add_item(self, n):
        """
        Adds an item to the priority queue
        """
        self.queue.append(n)
        self._sort_heap()

    def min_elem(self):
        """
        Returns the top min element in the heap, and erase it.
        """
        result = self.queue[1]
        self.queue[1] = self.queue[len(self.queue) - 1]
        del self.queue[len(self.queue) - 1]
        self._sort_heap()
        return result

    def __str__(self):
        if self.queue:
            return u''.join([str(i) + ',' for i in self.queue])
        else:
            return "Empty queue"

def main():
    """
    Heaps in python
    """
    min_heap = Heap()
    l = [4,5,9,1,10,11,12]
    print("Unsorted: ", l)
    #Heapsort it takes O(n log n) time
    for i in l:
        min_heap.add_item(i)
    for i, _ in enumerate(l):
        l[i] = min_heap.min_elem()
    print("Sorted:   ", l)
    #print(min_heap)
    #print(min_heap.min_elem())
    #print(min_heap)
        


if __name__ == '__main__': main()