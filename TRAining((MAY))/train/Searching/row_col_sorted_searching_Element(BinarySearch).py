def search(matrix,k):
    r=len(matrix)
    c=len(matrix[0])
    i,j=0,c-1
    while i<r or j>=0:
        if matrix[i][j]==k:
            return f"found at {i} ,{j}"
        elif k<matrix[i][j]:
            j-=1
        else:
            i+=1
    return "Not Found"
matrix=[[3,4,6,8],[5,7,9,10],[8,12,13,15],[20,23,26,28],[30,36,40,45]]
k=23
print(search(matrix,k))