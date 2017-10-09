#!/usr/bin/python3
import operator

def merge(left, right, compare=operator.lt):
    result = list()
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def mergesort(v, compare=operator.lt):
    if len(v) < 2:
        #single element
        return v[:]
    else:
        median = int(len(v) / 2)
        left  = mergesort(v[:median], compare)
        right = mergesort(v[median:], compare)
        return merge(left, right, compare)

def main():
    v = [3, 2, 4, 1, 5, 7, 6, 8, 9, 11]
    v = mergesort(v)
    print(v)

if __name__ == '__main__':
    main()