'''
Count vowels
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

For example, if s = 'hello', your program should print:

Number of vowels: 2

The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:
For example:
| Test        | Result                |
|-------------|-----------------------|
| Restaurant       | Number of vowels: 4   |
| Air      | Number of vowels: 2   |
'''

s = input()
voweels = 'aeiouAEIOU'
count = sum(1 for char in s if char in voweels)
print(f"Number of vowels: {count}")
