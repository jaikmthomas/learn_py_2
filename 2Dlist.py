#Playing with 2D list to obtain output as rows only
grid = [
    {1,2,3},
    [4,5,6],
    [7,8,9]
]
for row in grid:
    print(row)

#Playing with 2D list to obtain output containig every term
for row in grid:
    for col in row:
        print(col)