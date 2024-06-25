# boring arrays problem
"""You are given an array of size in one operation you can select any two elements from it, add their
absolute difference in your score
• Your task is to find and return an integer value, representing the maximum score
Note:
Assume 1 based indexing
The elements on which operation has been performed cannot be selected again.
Input Specification:
Input. An integer value N, representing the size of array A
Input? An integer array A
Output Specification:
Return an integer value, representing the maximum score
Sample Input:
4
1 2 3 4 
Output:
1 2 3 4
4
"""

n=int(input())
a=list(map(int,input().split()))
a.sort()
# print(a)
j,i=n-1,0
sum,diff=0,0
while i<=j:
    diff=abs(a[j]-a[i])
    # print(diff)
    sum+=diff            
    # print(sum)
    if i==j:
        break
    j-=1
    i+=1
print(sum)