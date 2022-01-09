# check if every row and column contains all numbers from 1 to n
matrix = [[1,2,3],[3,1,2],[2,3,1]]

# time comp --> O(N) space comp --> O(1)
def checkValid(matrix):
    n = len(matrix)


    for row in matrix:
        if set(row) != set(range(1, n+1)):
            return False

    # to get the column values of all the rows in matrix we can use zip(*matrix) --> column elements
    # zip combine the two lists or tuples togather --> print(list(zip(*matrix)))

    for col in zip(*matrix):
        if set(col) != set(range(1, n+1)):
            return False

    return True

ans = checkValid(matrix)
print(ans)
