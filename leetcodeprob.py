#find missing and repeating value in a 2d matrix from range 1 to n**2
"""You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each
integer appears exactly once except a which appears twice and b which is missing. The task is to
find the repeating and missing numbers a and b. Return a 0-indexed integer array ans of size 2
where ans[0] equals to a and ans[1] equals to b. 
"""
a=[]
for i in range(0,2):
    sub=[]
    # print("Enter the value for",i)
    for j in range(0,2):
        # print("Enter the value for",j)
        ele=int(input())
        sub.append(ele)
    a.append(sub)
    print(a)
print(a)
d={}
ans=[]
for i in range(0,2):
    for j in range(0,2):
        if a[i][j] not in d:
            d[a[i][j]]=1
        else:
            d[a[i][j]]+=1
            if d[a[i][j]]==2:
                ans.append(a[i][j])
print(d)
#missing
for i in range(1,4): #1 to n**2 +1
    if i not in d:
        ans.append(a[i][j])
print(d)
print(ans)