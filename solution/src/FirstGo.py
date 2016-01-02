'''
Solving the hackerrank The Love-Letter Mystery puzzle.

https://www.hackerrank.com/challenges/the-love-letter-mystery

---------------------

Problem Statement

James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can reduce the value of a letter, e.g. he can change d to c, but he cannot change c to d.
In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes a. Once a letter has been changed to a, it can no longer be changed.
Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.

Input Format

The first line contains an integer T, i.e., the number of test cases. 
The next T lines will contain a string each. The strings do not contain any spaces.

Constraints 
1<=T<=10 
1<= length of string <=104 
All characters are lower case English letters.

Output Format

A single line containing the number of minimum operations corresponding to each test case.

---------------------

Straight forwards I think

Created on 2 Jan 2016

@author: chris
'''

def solver(inputStrings):
    
    output = []
    
    for inputString in inputStrings:
        N = len(inputString)/2
    
        left = inputString[:N]
        right = inputString[-N:][::-1]
        
        operations = 0
        for lChar, rChar in zip(left, right):
            operations += abs(ord(lChar) - ord(rChar))
    
        output.append(operations)
    
    return output
    
if __name__ == '__main__':
    inputStrings = []
    
    for _ in range(input()):
        inputStrings.append(raw_input().strip())
     
    output = solver(inputStrings)
    
    for o in output:
        print o
