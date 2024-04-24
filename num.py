def pattern_x_with_numbers(n):
    if n % 2 == 0:
        n += 1  # Ensure odd number of rows for symmetry
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or i + j == n + 1:
                print(i, end='')
            else:
                print(' ', end='')
        print()

# Example usage with n = 5
pattern_x_with_numbers(5)
