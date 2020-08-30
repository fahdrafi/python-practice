def parity_brute_force(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def parity_remove_lowest_set_bit(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x &= x-1
    return result
