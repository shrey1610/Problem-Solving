# #find the distance of the given seat from the corner seats
"""Bruce is a newly hired employee at a company. The Office Management Department has given him
a desk number, which is stored in string S. He has also been handed a string array A. containing all
the N office desk numbers.
Array A also includes the symbol"-", which stands for the gap in the sitting arrangement. Comer
seats are those that are on either side of the gap. Your task is to help Bruce find and return an integer
value. representing how far he is from the nearest corner seat. Return 0, if he is in the corner seat..
Note:
There will always be at least one gap in the string array A
Desk number is always in a format of a number first followed by an English letter in uppercase
Assume 0-based indexing
Input Specification:
A string S. representing Bruce's newly assigned desk number.
Second line containing space separated strings showing the seat positions and gaps
Sample input:
3C
1A 2b - 3C 4D 
Output:
3C
1A 2B - 3C - 4D
0 
"""

# s=input()
# s1=list(input().split())
# # print(s1)
# a=[]
# for i in range(0,len(s1)):
#     if s1[i]=="-":
#         # print(s1[i])
#         a.append(i)
# # print(ind)

chair=input()
s=list(input().split())
# find Index
c_ind=s.index(chair)
z=999

# till end 
for i in range(0,c_ind):
    if s[i]=="-":
        if abs(c_ind-i)-1<z:
            z=abs(c_ind-i)-1
# right side 
for i in range(c_ind,len(s)):
    if s[i]=="-":
        if abs(c_ind)-1<z:
            z=abs(i-c_ind)-1
print(z)