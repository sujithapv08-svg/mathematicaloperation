def digital_root(n):
    n = abs(n)
    while n > 9:
        total = 0
        while n > 0:
            total = total + n % 10
            n = n // 10
        n = total
    return n

n = int(input("Enter a number: "))
print(digital_root(n))