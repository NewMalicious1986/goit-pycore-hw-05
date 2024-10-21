def caching_fibonacci(number):
    """
    Calculate the Fibonacci number at a given position using memoization.
    This function uses a nested helper function to compute the Fibonacci number
    at the specified position, caching intermediate results to improve performance
    for subsequent calls.
    Args:
        number (int): The position in the Fibonacci sequence to compute.
    Returns:
        int: The Fibonacci number at the specified position.
    """

    cache = {}

    def fibonacci(n):
        """
        Calculate the nth Fibonacci number using memoization.
        This function uses a cache to store previously computed Fibonacci numbers
        to optimize the calculation process.
        Args:
            n (int): The position in the Fibonacci sequence to compute.
        Returns:
            int: The nth Fibonacci number.
        """

        if n in cache:
            return cache[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci(number)

if __name__ == "__main__":
    print(caching_fibonacci(10))  # Output: 55
