#specizl fibonacci problem
"""Alex is exploring a series and she came across a special series, in which
f(N)=f(N-1)*f(N-1)+(N-2)*(N-2) mod 47
where f(0) = 1. f(1)=1
Your task is to help Alex find and return an integer value, representing the Nth number in this
special series.
Input Specification:
input1: An integer value N.
Output Specification:
Return an integer value, representing the Nt number in this special 
Output:
6
34
"""
n=int(input())
# recursion
# def f(n):
#     if n==0 or n==1:
#         return 1
#     return (f(n-1)*f(n-1)+(n-2)*(n-2))%47
# print(f(n))

# iterative 
x=[1,1]
ans=0
for i in range(2,n+1):  #from 2 because for index 0 and 1 it is given to return 1s
    ans=(x[i-1]*x[i-1]+(i-2)*(i-2))%47
    x.append(ans)
print(ans)