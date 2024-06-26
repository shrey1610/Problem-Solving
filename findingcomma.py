# finding commas problem
"""Liam works as a data analyst for a company that stores massive amounts of numerical data. He has
been tasked with determining how many commas are used when writing numbers in the range of 1
to N (inclusive) in a specific format
In this format, if numbers are more than four digits long, commas are used to separate the numbers
into groups of three, starting from the right for the representation of the number. Your task is to help
Liam find and return an integer value, representing the total number of commas used when writing
each integer in the range of 1 to N
Input Specification:
Input: An integer value N. representing the number range.
Output Specification:
Return an integer value, representing total number of commas used when writing each integer in the
range of 1 to N.
Sample Input:
5000
Sample Output:
4001
"""
n=int(input())
c,k,num,ans,s=1000,1,0,0,0
a=[]
if n<1000:
    print("0")
while c<n:
    m=c*1000
    num=min(n-c+1,m-c)
    ans=num*k 
    # print(ans)
    c=m
    k+=1
    s+=ans
print(s)