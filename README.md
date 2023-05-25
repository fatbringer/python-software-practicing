# software-practicing-python

Here i put codes that i wrote in the past as practice
either for online courses or for platforms like hackerrank or something

Here are some notable learnings


# Reading input from stdin
eg a = int(input()) 
this reads the input and convert into a int. Else it is a string. 

# strings
1) string.isalnum() 
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
print 'ab123'.isalnum()
True
print 'ab123#'.isalnum()
False

2) str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False

3) str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False

4) str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
