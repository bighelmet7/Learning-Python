"""Selection sort in python"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-

def selection_sort(v):
    """TIME COMPLEXITY Theta(n^2)"""
    for i in range(len(v)):
        mini = min(v[i:])
        min_index = v[i:].index(mini)
        v[i + min_index], v[i] = v[i], mini

def main():
    """type an unsorted vector"""
    v = [4,2,3,1]
    selection_sort(v)
    print(v)

if __name__ == '__main__':
    main()