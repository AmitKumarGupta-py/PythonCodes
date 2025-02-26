n = 5

# Upper half of the butterfly
for i in range(1, n+1):
    left = "*" * i
    # The number of spaces is 2*(n-i) to create symmetry
    spaces = " " * (2 * (n - i))
    print(left + spaces + left)

# Lower half of the butterfly
for i in range(n, 0, -1):
    left = "*" * i
    spaces = " " * (2 * (n - i))
    print(left + spaces + left)
