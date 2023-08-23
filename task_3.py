def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_fib = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_fib)
    return fib_series

def main():
    n = int(input("Enter the number of Fibonacci numbers you want to generate: "))
    fib_series = fibonacci(n)
    
    print("Fibonacci numbers:")
    for num in fib_series:
        print(num, end=", ")

if __name__ == "__main__":
    main()
