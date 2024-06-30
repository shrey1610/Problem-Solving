#maximum vowel count
"""Given a string s print the most frequent vowel that is present in the string as a output
Input Format:
A single line containing the string s
The input will be read form the STDIN by the candidate
Output:
Print a single character which represent the most frequent vowel in the given string
Output:
helloworld
{'e': 1, 'o': 2}
o 
"""
s=input()
d={}
mx=-999
v="aeiou"
ans=0
for i in s:
    if i in v:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
        if mx<d[i]:
            mx=d[i]
            ans=i
print(d)
print(ans)