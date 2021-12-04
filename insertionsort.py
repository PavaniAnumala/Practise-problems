
# time complexity O(n) already sorted, worst case = O(n^2) reverse sorted
if __name__ == '__main__':
    ele = [21,12,5,7,8]

    for i in range(len(ele)):

        val = ele[i]
        j=i
        while j>0 and ele[j-1]>val:
            ele[j]=ele[j-1]
            j = j-1
        ele[j] = val

    print("After sorted")
    print(ele)