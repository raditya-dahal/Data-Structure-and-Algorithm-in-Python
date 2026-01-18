'''
Write a class Person that has a member function hello()
The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:

For Example:
| Test        | Result                |
|-------------|-----------------------|
| p = Person('Matti') p.hello()        | Hello, world!         |
'''

class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello, my name is  {self.name}")