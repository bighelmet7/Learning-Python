#!/usr/bin/python

def binary_search(v, x, left, right):
    """Found x in a ascendent sorted list"""
    if left <= right:
        middle = int((left + right) / 2)
        if x < v[middle]:
            return binary_search(v, x, left, middle - 1)
        elif x > v[middle]:
            return binary_search(v, x, middle + 1, right)
        else:
            return middle
    else:
        return -1

def main():
    """Binary search"""
    v = [1,2,3,4,5,6,7,8,9,10]
    x = 5
    position = binary_search(v, x, 0, len(v) - 1)
    if position != -1:
        print("Element found", position)
    else:
        print("Element doesnt exists")


if __name__ == '__main__':
    main()