def fibonacci(n):
    """
    This function generates the first n Fibonacci numbers.
    """
    crlf = '\r\n'
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])        
    return fib

# Example usage
n = 1000
fib = fibonacci(n)
#print(fib)
for i in fib:
    print(i)