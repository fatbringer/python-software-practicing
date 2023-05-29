# software-practicing-python

Here i put codes that i wrote in the past as practice
either for online courses or for platforms like hackerrank or something

Here are some notable learnings

### non library specific
1) getattr(arr,command)(*n) --> from practice number 6.                    
the *n operator is iterating operator.                      
getattr will retrieve the type of the input and allow you to work on it like a variable                       
eg here, arr is a list, and command can be "append" or "pop".                   
getattr gets the variable type of arr, which is list.                 

### numpy
1) np_array = numpy.array(arr, float)  --> converts a list called arr into a numpy array, you can specify the value type. Eg float int double 
2) np.transpose 
3) np.matmul --> to do matrix multiplication on 2 matrices (max is 2 for this function)
4) np.array --> to convert a list into an array 
5) np.linalg.inv --> to calculate the inverse of a matrix
6)  @ operator --> usin the @ operator lets you do multiple matrix multiplcations in 1 line in that specified order                         
     eg   Pmatrix = np.linalg.inv( np.matmul(np.matmul(H_trans, R_inv), Hmatrix))              
          Pmatrix = np.linalg.inv( H_trans @ R_inv @ Hmatrix)              
          These 2 lines are equivalent in their operation             

### Reading input from stdin
1) eg a = int(input())  ---> this reads the input and convert into a int. Else it is a string. 

### strings
1) string.isalnum() 
2) str.isalpha()
3) str.islower()
4) str.isupper()
5) str.ljust(width, padding_chars)
6) str.rjust(width, padding_chars)
7) str.center(width, padding_chars)
8) str.join() --> see #https://www.w3schools.com/python/ref_string_join.asp 

### numbers (int, octa, hexadecimal, binary) 
normal = str(i)               
octal = format(i,'o')                   
hexa = format(i, 'X')              
binary = format(i, 'b')                 

        
### dictionary
1)  dictonary_name.items()  gives you key (key, value) tuples:

### collections  
import collections       
from collections import Counter   #https://www.geeksforgeeks.org/python-collections-module/    
> print(Counter(['B','B','A','B','C','A','B','B','A','C']))   #Counter gives you a dictionary                    
> {'B': 5, 'A': 3, 'C': 2}         

### sets vs list
sets only retain unique values, list retains whatever you put in        
scores_set = set(scores)  #set only retains unique values, you can convert a list into a set like that 

### itertools
itertools.product() 

