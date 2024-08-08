# A-21 : 21. Write a program that illustrates all bitwise operations in Python.

def bitwise_operations(a, b):
    print(f"a = {a}, b = {b}")
    print(f"Bitwise AND (a & b): {a & b}")
    print(f"Bitwise OR (a | b): {a | b}")
    print(f"Bitwise XOR (a ^ b): {a ^ b}")
    print(f"Bitwise NOT (~a): {~a}")
    print(f"Bitwise NOT (~b): {~b}")
    print(f"Bitwise LEFT SHIFT (a << 1): {a << 1}")
    print(f"Bitwise RIGHT SHIFT (a >> 1): {a >> 1}")
    print(f"Bitwise LEFT SHIFT (b << 1): {b << 1}")
    print(f"Bitwise RIGHT SHIFT (b >> 1): {b >> 1}")

a = 1
b = 0

bitwise_operations(a, b)