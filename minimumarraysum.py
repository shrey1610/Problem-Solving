#minimum array sum
"""Paul is given an array A of length N.He must perform the following operation on the array
sequentially:
• Choose any two integers from the array and calculate their average
• If an element is less then the average, update it to 0. However,if element is greater than or equal
To average, he need not update it.
• Your task is to help Paul find and return an integer value , representing the minimum possible
sum of all the elements in the array by performing the above operations
Note: An exact average should be calculated, even if it results in a decimal
Input format:
Input1: An integer value N, representing the size of the array A.
Input2 :An integer array A.
Output format:
 Return an integer value representing The minimum possible sum of all the elements in the array by
Output
12 16 22 2
22
16 
22
"""


l=list(map(int,input().split()))
max1,max2,sum=0,0,0
for i in l:
    if max1<i:
        max1=i
print(max1)
for i in l:
    if i==max1:
        continue
    else:
        if max2<i:
            max2=i
print(max2)

avg=(max1+max2)/2
for i in l:
    if avg<i:
        sum+=i
print(sum)