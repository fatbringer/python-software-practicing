https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------


#%%

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())
pat = ".|."

for i in range (1, N//2 + 1):
    pat_stack = pat * (2*i - 1)
    dashes_and_pat_stack = pat_stack.center(M,"-")
    print(dashes_and_pat_stack)
    
    if i == N//2: 
        welcome_text = "WELCOME".center(M,"-")
        print(welcome_text)
    

    
for i in reversed(range(1, N//2 + 1)):
    pat_stack = pat * (2*i - 1)
    dashes_and_pat_stack = pat_stack.center(M,"-")
    print(dashes_and_pat_stack)
        
