from math import factorial

def vowel_perm(s):
    c = sum(1 for ch in s if ch.lower() not in "aeiou")
    return factorial(c) if c > 0 else 0
print(vowel_perm("ABC"))
print(vowel_perm("CDF"))
print(vowel_perm("AEI"))