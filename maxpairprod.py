# maximum pair product problem
"""Noah is given an integer array A of length N. He must perform the following operations:
• Select any Integer pair having sum equal to 18 from the array.
• Select the pair with maximum product such that the first element of the pair is greater than the
second element of the pair.
• Your task is to help Noah find and return a pair in the form of an integer array, which satisfies the
mentioned conditions.
Input Specification:
Input1: An Integer value N, representing the size of array A.
Input2: An integer array A.
Output Specification:
Return a pair in the form of an integer array, which satisfies the mentioned
Sample input:
8
11 12 2 8 10 11 9 8
Sample output: 
10 8 
"""
n=int(input())
a=list(map(int,input().split()))
prod,maxi,a1,b1,s=0,0,0,0,0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==18:
            if a[i]>a[j]:
                prod=a[i]*a[j]
                if prod>maxi:
                    maxi=prod
                    a1,b1=a[i],a[j]
print(a1,b1)