def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")