"""
# CHAPTER 6 EXERCISE 1
'''
Student Grade Lookup (Dictionary) Exercise

A teacher wants a quick way to store and look up student grades.

Create a program that:
- Stores student names and grades in a dictionary
- Lets the user choose from multiple actions:
    add/update a grade
    search a student’s grade
    print all students and grades
    loop until they select 0 (zero)

- If the student is not found, print a message

Example data
"Anna": 5
"Mikko": 4
"Sara": 3

'''

# Hint! Use a dictionary and while loop for example!


"""
grades = {
    "Anna": 5,
    "Mikko": 4,
    "Sara": 3
}

# Menu loop
while True:
    print("\n--- Student Grade Lookup ---")
    print("1. Add or update a grade")
    print("2. Search a student's grade")
    print("3. Print all students and grades")
    print("0. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        try:
            grade = int(input("Enter grade (0-5): "))
            if 0 <= grade <= 5:
                grades[name] = grade
                print(f"Grade for {name} has been set to {grade}.")
            else:
                print("Grade must be between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number for the grade.")
            
    elif choice == "2":
        name = input("Enter student name to search: ")
        if name in grades:
            print(f"{name} has a grade of {grades[name]}.")
        else:
            print(f"{name} not found.")
            
    elif choice == "3":
        print("\nAll students and grades:")
        for student, grade in grades.items():
            print(f"{student}: {grade}")
            
    elif choice == "0":
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("Invalid option. Please choose from the menu.")