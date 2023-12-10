def count_bits(n: int):
    num_bits = 0
    while n:
        num_bits += n & 1
        n >>= 1
    return num_bits


print(count_bits(5))