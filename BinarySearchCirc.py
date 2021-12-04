def searchCircularList(nums,key):
    (left,right) = (0,len(nums)-1)
    while left < right:
        mid = (left + right ) //2

        if(nums[mid] == key):
            return mid
        
        if (nums[mid]<=nums[right]):

            if(nums[mid]<key<=nums[right]):
                left = mid - 1
            else:
                right = mid + 1
        else:
            if(nums[mid]>key>=nums[left]):
                right = mid -1
            else:
                left = mid + 1

if __name__ == '__main__':
 
    nums = [9, 10, 2, 5, 6, 8]
    key = 5
 
    index = searchCircularList(nums, key)
 
    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')
 