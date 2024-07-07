#sub array with max sum problem  (this question is famously called as kadanes algorithm)
"""You are given a list of integers, and your task is to find the subarray with the maximum sum. Write
a function or method to solve this problem efficiently and return the maximum sum.

"""
# n=int(input())
nums=list(map(int,input().split()))
s,mx=0,0
for i in nums:
    if i<0:
        s=0
    else:
        s+=i
        if mx<s:
            mx=s
print(mx)