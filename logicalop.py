def logical_or(a, b):
    result = 0
    place = 1
    while a > 0 or b > 0:
        bit_a = a % 2
        bit_b = b % 2
        if bit_a == 1 or bit_b == 1:
            result = result + place
        a = a // 2
        b = b // 2
        place = place * 2
    return result

a = int(input("Enter A: "))
b = int(input("Enter B: "))
print(logical_or(a, b))