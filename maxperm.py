from math import factorial

def max_perm(arr, n):
    b = 0
    for s in arr:
        k = sum(1 for ch in s if ch.lower() not in "aeiou")
        if k > 0:
            b = max(b, factorial(k))
    return b
print(max_perm(["eio"],1))