"""Eve has a string 5 containing lowercase English letters. She wants to transform this string into a
Magic String, where all the characters in the string are the same. To do so, she can replace any letter
in the string with another letter present in that string. 6
Your task is to help Eva find and return an integer value, representing the minimum number of steps
required to form a Magic String. Return 0, if 5 is already a Magic String
Input Specification:
Input: A string 5, containing lowercase English letters.
Output Specification:
Return an integer value, representing the minimum number of steps required to form a Magic
String. Return O, If S is already a Magic String
Sample input:
aaabbbccdddd
Sample output:
8 
"""
s=input()
d={}
mx=-999
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    if d[i]>mx:
        mx=d[i]
print(len(s)-mx)