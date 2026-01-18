'''Arithmetic
Write a program that takes two integers, a and b, as input.
Your program should compute and display:
The sum of a and b
The difference when b is subtracted from a
The product of a and b
The quotient when a is divided by b
The remainder when a is divided by b
The result of log10 a
The result of ab
a
b
The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column
For example:
| Test        | Result                |
|-------------|-----------------------|
| 10 2        |  10 + 2 is 12         |
|             | 10 - 2 is 8           |
|             | 10 * 2 is 20          |
|             | 10 / 2 is 5.0         |
|             | 10 % 2 is 0           |
|             | 10 to the power of 2 is 100 |
|-------------|-----------------------|
| 4 2         | 4 + 2 is 6          |
|             | 4 - 2 is 2           |
|             | 4 * 2 is 8           |
|             | 4 / 2 is 2.0         |
|             | 4 % 2 is 0           |
|             | 4 to the power of 2 is 16  |
'''

a = int(input())
b = int(input())


print(f"{a} + {b} is {a + b}")
print(f"{a} - {b} is {a - b}")
print(f"{a} * {b} is {a * b}")
print(f"{a} / {b} is {a / b}")
print(f"{a} % {b} is {a % b}")
print(f"{a} ^ {b} is {a ** b}")