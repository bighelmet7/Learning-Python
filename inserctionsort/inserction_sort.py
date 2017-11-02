"""Inserction sort in python"""
#!/usr/bin/python3

def inserction_sort(v, n):
    for k in range(1, n):
        t = k - 1
        while t >= 0 and v[t + 1] < v[t]:
            v[t + 1], v[t] = v[t], v[t + 1]
            t -= 1

def main():
    """Time complexity of Theta(n^2)"""
    v = [4,2,3,1]
    inserction_sort(v, len(v))
    print(v)

if __name__ == '__main__':
    main()
