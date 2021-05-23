import gcd

# Returns the lowest common multiple of two integers, x and y.
# The lowest common multiple, m, is the smallest positive integer such that m divides x and y.
def lcm(x, y):
    # Using lcm(x, y) = |xy| / gcd(x, y)
    return int(abs(x * y) / gcd.gcd(x, y))