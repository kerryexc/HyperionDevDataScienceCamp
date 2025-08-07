
# a tuple is ordered and unchangeable

# we will have four rows

num_pad = ((1, 2, 3), 
           (4, 5, 6), 
           (7, 8, 9), 
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# the above will print a grid of rows and columns