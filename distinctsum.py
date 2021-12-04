
def findCombinations(A,n,k,subarray,out=()):
    if(len(A)==0 or k>n):
        return
    if(k==0):
        subarray.add(out)
        return
    
    for i in reversed(range(n)):
        findCombinations (A,i,k-1,subarray,(A[i],)+out)


def getDistinctCombinations(A,k):
    subarray = set()
    findCombinations(A,len(A),k,subarray)
    return subarray


if __name__ == '__main__':
 
    A = [1, 2, 3]
    k = 2
 
    # process elements from right to left
    subarrays = getDistinctCombinations(A, k)
    print(subarrays)