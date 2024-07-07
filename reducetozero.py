#reduce to zero and return the corresponding value
"""Dev loves the number zero. Dev gives Andrew two integers X and Y and asks him to perform the
steps below on X and Y. until the value of Y has been reduced to zero. The below steps should be
followed sequentially:
1. If X<="" p="" style="box-sizing: inherit;">
2. If Y=0. then return X
3. Otherwise, let T =X-Y.
4. Set X-Y and then set Y=T
5. Repeat from step 1.
Your task is to help Andrew find and return an integer value, representing the value of X, when the
value of Y has been reduced to zero.
Note: At least one of the X or Y will be a non-zero integer
Input Specification:
Input 1: An Integer value X. representing the first number.
Input2: An integer value Y, representing the second number
Sample Input:
48
18
Output:
48
18
6 
"""
x=int(input())
y=int(input())
temp=0
while y!=0:
    if x<=y:
        temp=x #other way to swap --> x,y=y,x
        x=y
        y=temp
    if y==0:
        break
    t=x-y
    x=y
    y=t
print(x)