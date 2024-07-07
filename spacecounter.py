#space counter problem
"""You have been gives the task of making the counter on a social media platform more userfriendly.your task is to find and return an integer value representing the count of the number of
spaces in a gives string S.
Input:
A string:
Output:
Return an integer value representing the count of the number of space in a given string S. 
Output :
hi hello hey
2 
"""
# logic 1
str=input().split()
print(len(str)-1)


#another logic
# str=input()
# count=0
# for i in str:
#     if i == " ":
#         count+=1
# print(count)