rows = 5  # Number of rows for the pyramid

for i in range(rows):
    # Loop to print 'x' characters
    for k in range(rows - i - 1):
        print(' ', end='')
    for j in range(i+1):
        print('x ', end='')
    print()  # Move to the next line after each row
