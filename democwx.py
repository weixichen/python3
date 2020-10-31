#__author: cad
#date: 2020/9/29
name = input("Name:")
age = input("Age:")
job = input("Job:")
salary = input("salary:")
MSG = '''
------------------------info of %s-------------------------
Name: %s
Age: %s
Job: %s
Salary: %s
------------------------end---------------------------------
''' % (name, name, age, job, salary)
print(MSG)