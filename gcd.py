import math

def gcd(x, y):
    # Ensures x is non-negative
    # Notice that gcd(x, y) = gcd(-x, y) since x only changes by a factor of -1 (which doesn't change the gcd)
    if x < 0:
        return gcd(-x, y)

    # Ensures y is non-negative
    if y < 0:
        return gcd(x, -y)

    # This ensures that x >= y
    if y > x:
        return gcd(y, x)

    # And this ensures that at least one of x, y is strictly positive
    # If both are 0, then all integers divide both x and y, so gcd(x, y) is not finite
    if y == x and y == 0:
        return math.inf

    # If y = 0, then x divides y (and x divides x), so gcd(x, y) = gcd(x, 0) = x
    if y == 0:
        return x
    
    # If this point is reached, we can assume that x >= y and x, y >= 0 and one of x, y non-zero
    # So now we can write x = yq + r, then gcd(x, y) = gcd(y, r)
    return gcd(y, x % y)
