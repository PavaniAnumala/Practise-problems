import sys

A = [-10, -3, 5, 6, -2]

max1 = A[0]
max2 = -sys.maxsize

min1 = A[0]
min2 = sys.maxsize

for i in range(1,len(A)):
    
    if(max1<A[i]):
        max2 = max1
        max1 = A[i]
    elif(max2<A[i]):
        max2 = A[i]

    if(min1>A[i]):
        min2 =min1
        min1=A[i]
    elif(min2>A[i]):
        min2 = A[i]
print(f"max1={max1},max2={max2}")

print(f"min1={min1},min2={min2}")
