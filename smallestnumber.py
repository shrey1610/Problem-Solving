# smallest number
"""Prince participated in three olympiads at school and received marks for all of them he is interested
In finding out the lowest marks he obtained among the three olympiads.write a program to find the
minimum marks
Example:
Input: 50 66 23
Output: smallest number is 23 
"""
a=list(map(int,input().split()))
mini=999
for i in a:
    if i<mini:
        mini=i
print(mini)