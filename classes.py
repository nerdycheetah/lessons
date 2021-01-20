# adding commit to test git changes
# class Coffee:
#     def __init__(self, coffee_type:str, amount:int=1):
#         self.coffee_type = coffee_type
#         self.amount = amount
#     def __str__(self):
#         return f'{self.amount} cup(s) of {self.coffee_type} coffee'
#     def __repr__(self):
#         return f'Coffee(\'{self.coffee_type}\', {self.amount})'

# aroosh_coffee = Coffee('African Roast', 2)
# wesley_coffee = Coffee('French Roast', 3)
# print('\n')
# print('str method:')
# print(aroosh_coffee)

# print('\nrepr method:')
# print(repr(aroosh_coffee))
# print('\n')

# range_object = range(5, -5, -1)
# print(repr(range_object))
# print(repr(wesley_coffee))



# range_object = range(5)
# print(range_object)

class Student:
    def __init__(self, name:str, age:int, grade:int):
        self.name = name
        self.age = age
        self.grade = grade
        # grade = 1st grade, 2nd grade etc.
    def __str__(self):
        return f'{self.name} is {self.age} years old and is in {self.grade}th grade. '
        # Aroosh is 12 years old and is in 6th grade.
    def __repr__(self):    
        return f'Student({self.name}, {self.age}, {self.grade}) '
# aroosh_student = Student('Aroosh', 12, 6)
# print('str method:')
# print(aroosh_student)
# print('\n')
# print('repr method:')
# print(repr(aroosh_student))
# print('\n')
        

# class Car:
#     def __init__(self, n_doors, n_seats, drivetrain_type):
#         self.n_doors = n_doors
#         self.n_seats = n_seats
#         self.drivetrain_type = drivetrain_type 

# class Coupe(Car):
#     def __init__(self, n_seats, drivetrain_type):
#         self.n_seats = n_seats
#         self.drivetrain_type = drivetrain_type
#         Car.__init__(2, self.n_seats, self.drivetrain_type)
        
# class Sedan(Car):
#     def __init__(self, n_seats, drivetrain_type):
#         self.n_seats = n_seats
#         self.drivetrain_type = drivetrain_type
#         Car.__init__(4, self.n_seats, self.drivetrain_type)

# class Person:
#     def __init__(self, name, age, ethnicity):
#         self.name = name
#         self.age = age
#         self.ethnicity = ethnicity

# class Employee(Person):
#     def __init__(self, name, age, ethnicity, company, position):
#         self.company = company
#         self.position = position
#         Person.__init__(self, name, age, ethnicity)
    
# aroosh = Person('Aroosh', 12, 'Indian')
# aroosh_dev = Employee('Aroosh', 12, 'Indian', 'Microsoft', 'Software Engineer')




