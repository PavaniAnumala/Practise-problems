

def is_safe(mat,r,c):
    #checking for same column
    for i in range (r):
        if(mat[i][c]=='Q'):
            return False
    
    # checking for '/'diagonal

    for i in range(r):
        for j in range(c):
            if(mat[i][j]=='Q'):
                return False
            i -= 1
            j += 1
    #checking for '\' diagonal
    for i in range(r):
        for j in range(c):
            if(mat[i][j] == 'Q'):
                return False
            i -=1
            j += 1
    return True




def printSolution(mat):
    for r in mat:
        print(str(r).replace(',', '').replace('\'', ''))
    print()


def nqueen(mat,r):
    if r == len(mat):
        printSolution(mat)

        return

    for i in range(len(mat)):

        if is_safe(mat,r,i):
            mat[r][i] = 'Q'
        nqueen(mat, r + 1)
        # backtrack and remove the queen from the current square
        mat[r][i] = '–'




if __name__ == '__main__':
    n = int(input(""))
    mat = []
    #mat = [a.append(for j in range(0)) for j in range(0,n) for i in range(0,n)]
    for i in range(0,n):
        mat.append(['_' for j in range(0,n)])
    print(len(mat))
    nqueen(mat,0)
    
    