def printCombinations(nums,i,total,sum_left):

    prev_number = nums[i-1] if i>0 else 1

    for k in range(prev_number,total+1):
        nums[i] = k
        print(i)

        if(sum_left>k):
            printCombinations(nums,i+1,total,sum_left-k)
        
        if(sum_left==k):
            print(nums[:i+1])



def findCombinations(total):
    nums = [0]*total
    starting_index = 0
    printCombinations(nums,starting_index,total,total)



if __name__ == '__main__':
 
    total = 5
    findCombinations(total)