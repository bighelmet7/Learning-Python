""" this is quick power method """
#!/usr/bin/python3

def quick_power(x, n):
    """time complexity of O(log n)"""
    if n == 0: return 1
    else:
        y = quick_power(x, int(n / 2))
        if n % 2 == 0: return y * y
        else:          return x * y * y

def main():
    x, n = 2, 5
    print(quick_power(x, n))

if __name__ == '__main__':
    main()
