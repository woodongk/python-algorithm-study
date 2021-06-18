def BE2ndDiagonal(strArr):
    # code goes here
    n = len(strArr)
    m = len(strArr[0])

    for i in range(n):
        for j in range(m):
            if (i == j):
                print(mat[i][j], end=", ")

    for i in range(n):
        for j in range(m):
            if ((i + j) == (n - 1)):
                print(mat[i][j], end=", ")

    return strArr
