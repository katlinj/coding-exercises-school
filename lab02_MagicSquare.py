""""
A magic square is a 2D square grid of numbers such that the sum across any row or column is the same.
For example,
8 6 1
3 5 7
4 9 2
The sum across all rows and columns is 15.

This program determines whether a given square grid of numbers is a magic square or not.

Input format:
    First line: integer M that indicates the number of testcases.
    Each testcase starts with integer S which indicates the length of the side of the grid.
    S lines will follow, each containing S space-separated integers.

"""





def isMagicSquare(side):
    checkColumns = True
    Result = 0
    square = {}
    total = 0
    for i in range(side):
    #checking the sum of rows and getting input
        square[i] = list(map(int, input().rstrip().rsplit()))
        if i == 0:
            total = sum(square[i])
        if total == sum(square[i]):
            continue
        elif total != sum(square[i]):
            checkColumns = False
    if checkColumns == True:
    #checking the sum of each column
        for i in range(side):
            columnTotal = 0
            for row in square:
                columnTotal += square[row][i]
            if columnTotal != total:
                result = "No magic"
                return result
        result = "Magic square"
        return result
    elif checkColumns == False:
        result = "No magic"
        return result
        


testcases = int(input())
decision = []
for i in range(testcases):
    side = int(input())
    decision.append(isMagicSquare(side))
for k in decision:
    print(k)
    