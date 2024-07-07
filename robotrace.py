# robot race problem
"""There is a robot race happening between two robots named Robotop and Robocop. Both the robots
reach the starting point to begin the race on a Circular track
• Race starts at time T = 0 seconds. Robotop starts the race at T = Xth second and takes. exactly N
seconds to complete one lap. On the other hand. Robocop starts the race at T = Yth second and
takes exactly M seconds to complete one lap.
• Your task is to find and return an integer value, representing the least time T (in seconds) at
which these two robots meet each other again at the starting point.
Sample Input:
2 3 1 4
Sample Output:
5 
"""
x,n,y,m=map(int,input().split())
# print(x,n,y,m)
# print(abs(x*m-y*n))  #zubair cross multiplication logic



time=max(x,y)
while True:
    if time>=x and (time-x)%n==0 and time>=y and (time-y)%m==0:
        print(time)
        break
    time+=1
