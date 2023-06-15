def fibonacci_series(n):
    # Check if the input is valid
    if n <= 0:
        print("Invalid input. The number of terms should be a positive integer.")
        return

    # Handle the special case for the first two terms
    if n == 1:
        fibonacci_list = [0]
    elif n == 2:
        fibonacci_list = [0, 1]
    else:
        # Generate the Fibonacci series
        fibonacci_list = [0, 1]
        while len(fibonacci_list) < n:
            next_num = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_num)

    # Print the Fibonacci series
    for num in fibonacci_list:
        print(num, end=" ")

# Prompt the user to enter the number of terms
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Call the function to print the Fibonacci series
fibonacci_series(num_terms)
