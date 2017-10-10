#!/usr/bin/python3
"""
Write an efficient function

def first_occurrence(x, v);
that returns the position of the first occurrence of x in the vector v. If x does not belong to v, return a -1.

Precondition

The vector v is sorted in nondecreasing order. (non-decreasing sequence, x(n+1) >= x(n))

Observation You only need to submit the required procedure; your main program will be ignored.
"""
def position(v, x, left, right):
    if left <= right:
        median = int((left + right) / 2)
        if x < v[median]:
            return position(v, x, left, median - 1)
        elif x > v[median]:
            return position(v, x, median + 1, right)
        else:
            if median - 1 >= 0:
                repeated_position = position(v, x, left, median - 1)
                if repeated_position != -1:
                    return repeated_position
            return median
    return -1

def first_occurrence(x, v):
    return position(v, x, 0, len(v))

def main():
    v = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
    x = 2
    position = first_occurrence(x, v)
    if position != -1:
        print("Element found in position: ", position)
    else:
        print("Element not found")

if __name__ == '__main__':
    main()