# generated numbers problem
"""You have a jar which initially contains N marbles. You can perform the below operations in any
order:
1. Taking out A number of marbles from the jar.
2. Taking out B number of marbles from the jar.
Your task is to find and return an integer value, representing the total number of unique positive
number of marbles that can be left behind by performing these operations, including the initial
number of marbles.
Note:
You can perform the above operations any number of times and in any order keeping in mind that
the jar should never become empty.
Input Specification:
A single line containing space seperated integers N,A,B #10 3 5
Output:
6 
"""
n,a,b=map(int,input().split())
c=0
a1=n//a
b1=n//b
for i in range(a1+1):
    for j in range(b1+1):
            if i*a + j*b <10:
                c+=1
print(c)