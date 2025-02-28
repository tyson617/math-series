def fibonacci(n):
    """
    Return the nth value in the Fibonacci series.
    Fibonacci series starts with 0, 1 and each subsequent number is the sum of the two preceding ones.
    :param n: The index (zero-based) of the Fibonacci sequence to retrieve.
    :return: The nth Fibonacci number.
    """
    # Check if the input is a valid non-negative integer
    if n < 0:
        raise ValueError("Index must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize the first two numbers of the Fibonacci sequence
    a, b = 0, 1
    
    # Loop to compute the Fibonacci number iteratively
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update the values of a and b
    return b

def lucas(n):
    """
    Return the nth value in the Lucas series.
    Lucas series starts with 2, 1 and follows the same recursive pattern as Fibonacci.
    :param n: The index (zero-based) of the Lucas sequence to retrieve.
    :return: The nth Lucas number.
    """
    # Check if the input is a valid non-negative integer
    if n < 0:
        raise ValueError("Index must be a non-negative integer")
    elif n == 0:
        return 2  # First number of the Lucas sequence
    elif n == 1:
        return 1  # Second number of the Lucas sequence
    
    # Initialize the first two numbers of the Lucas sequence
    a, b = 2, 1
    
    # Loop to compute the Lucas number iteratively
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update the values of a and b
    return b

def sum_series(n, first=0, second=1):
    """
    Return the nth value in a series defined by the first two numbers.
    Defaults to Fibonacci series (0, 1) but can be used for Lucas numbers (2, 1) or other sequences.
    :param n: The index (zero-based) of the sequence to retrieve.
    :param first: The first value of the sequence (default is 0 for Fibonacci).
    :param second: The second value of the sequence (default is 1 for Fibonacci).
    :return: The nth number in the series.
    """
    # Check if the input is a valid non-negative integer
    if n < 0:
        raise ValueError("Index must be a non-negative integer")
    elif n == 0:
        return first  # Return the first value of the series
    elif n == 1:
        return second  # Return the second value of the series
    
    # Initialize the first two numbers of the series
    a, b = first, second
    
    # Loop to compute the series number iteratively
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update the values of a and b
    return b
