def fibonacci_sequence():
    n = int(input("How many terms do you want in the Fibonacci sequence? "))
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci_sequence()
