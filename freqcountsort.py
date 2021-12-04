 def findFrequency(nums,left,right,freq):
     if(left>right):
         return
     if(nums[left]==nums[right]):

         count = freq.get(nums[left])

         if count == None:
             count = 0
         freq[nums[left]] = count + (right-left +1)
         mid = (left+right)//2

         findFrequency(nums,left,mid,freq)
         findFrequency(nums,mid+1,right,freq)
 
 if __name__ == '__main__':
 
    nums = [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]
 
    # find the frequency of each element in the list and store it in a dictionary
    freq = {}
    findFrequency(nums, 0, len(nums) - 1, freq)
    print(freq)
 