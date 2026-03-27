n = 7
for i in range(1, n+1):
    print("#" * i)
    
    n = 8

for i in range(n):        # rows
    for j in range(n):    # columns
        print("#", end=" ")
    print()               # next line after each row

n = 8
for i in range(n):
    print("# " * n)
