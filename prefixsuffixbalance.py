# prefix suffix balance problemn
"""You are given an array A of N integers. The array A can be divided into two parts: the first part
consists of the first 'l' elements of A (where ranges from 1 to N), and the second part consists of the
last (N-i) elements of A
• Your task is to find and return a new array named result of the same size as A, where each
element of result[i] represents the absolute difference between the sum of the elements in the first
part of A and the sum of the elements in the second part of A
Note: For i= N,N-i=0.So, consider the sum of last N-i integers as O in this case
Input Specifications:
input1: An integer value representing the size of the array A.
Input2: An integer array A.
Output Specification:
Return a new integer array named result of the same size as A, where each element of result(i)
represents the absolute difference between the sum of the elements in the first part A and the sum of
the elements in the second part of A
Sample Input:
5
1 2 3 4 5
Sample Output:
 [13, 9, 3, 5, 15] 
"""
n=int(input())
a=list(map(int,input().split()))
sr,sl=0,0
a1=[]

#with using 2 for loops
# for i in range(len(a)):
#     for j in range(0,i+1):
#         sl+=a[j]
#     for k in range(i+1,n):
#         sr+=a[k]
#     diff=abs(sr-sl)
#     a1.append(diff)
#     sl,sr=0,0
# print(a1)

# without using 2 loops
tsum=0
for i in a:
    tsum+=i
# print(tsum)
currentsum=0
for i in a:
    sl+=i
    sr=tsum-sl 
    currentsum=abs(sr-sl)
    a1.append(currentsum)
print(a1)