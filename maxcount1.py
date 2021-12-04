def findIndexofZero(A):
    max_count = 0
    count = 0
    pre_zi = -1
    max_in = -1

    for i in range(len(A)):
        if(A[i] == 1):
            count +=1
        else:
            count = i-pre_zi
            pre_zi = i
        
        if(count > max_count):
            max_count = count
            max_in =pre_zi

    return max_in
        



if __name__ == '__main__':
 
    A = [0, 0, 1, 0, 1, 1,  1, 0, 1, 1]
 
    index = findIndexofZero(A)
    if index != -1:
        print("Index to be replaced is", index)
    else:
        print("Invalid input")