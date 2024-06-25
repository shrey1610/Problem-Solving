# best grades problem
"""Andrew has a string consisting of lowercase English letters representing respective grades of to
students in his class. His grade is at Pth index. He can swap any two adjacent grades
• Your task is to help Andrew find and return a string value, representing maximized grade by
bringing lexicographically smallest character on the Pth index after doing at most K swaps
Sample Input:
abcdefg
3
2
Sample Output:
cbaabcdefg
"""
a=input()
a1=list(a)
# print(a1)
p=int(input())
k=int(input())
mini=999
if abs(p-k-1)>=0:
    st=abs(p-k-1)
if p+k<len(a1):
    e=p+k
# print(st,e)
for i in range(st,e):
    mini=min(ord(a1[i]),mini)
    
store=a1[p-1]    #based on 1 indexing, it will be a1[p] if its 0 based indexing
a1[p-1]=a1[a1.index(chr(mini))]
a1[a1.index(chr(mini))]=store
# print(mini)
print(''.join(a1))