#peak element finder
'''
Description: You are given an N- dimensional array arr[]. A peak element in the array 
is defined as an element whose value is greater than or equal to its neighboring 
elements (if they exist). Your task is to find the index of any peak element in the given 
array
Note: use 0-based indexing
Input:
An integer representing the number of elements in the array. N space-separated 
integers, denoting the elements of the array.
N space-separated integers ,denoting the elements of the array arr[]
Sample Input:
5
1 3 20 4 1
Sample Output:
2
'''

n=int(input())
a=list(map(int,input().split()))
mp=0
for i in range(0,n-1):
    if a[i]>(a[i+1]) and a[i]>(a[i-1]):
        p=a[i]
        if mp<p:
            mp=p #for value
            res=i #for index
# print(mp) #element
print(res) #index value