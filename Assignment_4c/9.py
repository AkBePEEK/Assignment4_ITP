def countGoodNumbers(n: int) -> int:
    MODULO = 10 ** 9 + 7

    # Define the power function to calculate (x^n) % MODULO using binary exponentiation.
    def my_pow(base, exponent):
        result = 1
        while exponent > 0:
            # If exponent is odd, multiply the result with base.
            if exponent % 2 == 1:
                result = (result * base) % MODULO
            # Square the base and reduce the exponent by half.
            base = (base * base) % MODULO
            exponent //= 2
        return result

    # Number of primes at odd positions is 5 (2,3,5,7). Hence, we use 5 as the base.
    # Number of evens at even positions is 4 (0,2,4,6,8). Hence, we use 4 as the base. Even positions are considered 0-indexed here.
    # The +1 is needed when n is odd, to calculate 5 raised to the (n//2 + 1).
    return (my_pow(5, (n + 1) // 2) * my_pow(4, n // 2)) % MODULO


print(countGoodNumbers(50))