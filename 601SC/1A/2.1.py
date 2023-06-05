#Write the definition of a Python procedure fib, such that fib(n) returns
#the nth Fibonacci number. Recall the definition of fib
#⎧ (n):
#⎨ 0 if n = 0
#fib(n) = 1 if n = 1
#⎩ fib(n−1) + fib(n−2) if n > 1

def fib(n):
    if n <= 0:
        raise ValueError("Invalid input. n must be a positive integer.")

    # Base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1

    # Calculate Fibonacci number iteratively
    fib_minus_two = 0
    fib_minus_one = 1
    fib_current = None

    for _ in range(2, n):
        fib_current = fib_minus_two + fib_minus_one
        fib_minus_two = fib_minus_one
        fib_minus_one = fib_current

    return fib_current

print(fib(5))
