
def printSpiral(mat):

    #base condition 
    if(not mat or not len(mat)):
        return
    
    left = top = 0
    bottom = len(mat)-1
    right = len(mat[0])-1

    
    while True:
        #printing top row
        if(left>right):
            break

        for i in range(left,right+1):
            print(mat[top][i],end = ' ')
        top = top+1


        #printing last column
        if(top>bottom):
            break

        for i in range(top,bottom+1):
            print(mat[i][right],end = " ")
        
        right = right-1


        #printing bottom row

        if(left > right):
            break

        for i in range(right,left-1,-1):
            print(mat[bottom][i],end = ' ')
        bottom = bottom-1

        #printing first column

        if(top>bottom):
            break

        for i in range(bottom,top-1,-1):
            print(mat[i][left],end = ' ')
        left = left +1 






        

    
    


     

if __name__=='__main__':
    mat = []
    n=int(input())
    for i in range(n):
        a = []
        for j in range(n):
            k = int(input())
            a.append(k)
        mat.append(a)
    printSpiral(mat)