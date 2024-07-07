"""prime factors of a positive integer are the prime numbers that divide that integer exactly.
given an array arr of n integer and a positive integer num.
let's suppose prime factorization of num is
Sum of numbers in array arr at indices of prime factors of number num is:
Output format:
Print the sum that was mention in the problem statement 
"""

def pf(n):
    ans=[]
    i=2
    while i<=n:
        if n%i==0:
            ans.append(i)
            n=n//i
        else:
            i+=1
    return ans
ans =pf(6)
s=0
a=[11,12,13,14,15,16]
for i in ans:
    s=s+a[i]
print(s)
