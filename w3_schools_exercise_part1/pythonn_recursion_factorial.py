def is_prime_recursive(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor - 1)

# Example usage
print(is_prime_recursive(7))   # True
print(is_prime_recursive(10))  # False
