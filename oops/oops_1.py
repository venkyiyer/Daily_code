class Person:
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print("We are inside the init method")

	def __repr__(self):
		return f'Hi. My name is {self.name} and my age is {self.age}'
	# def __del__(self):
	# 	print("We are deleting the object")


a = Person("Venkatesh", 30)
# Python allows creating data members on the fly for a particular object
# a.name = "Venkatesh"
# a.age = 30
# del a
# print(a.name, a.age)

b = Person("Radha", 27)
print(b.name, b.age)

# But if we change the data member value outside init, it will overwrite the value specified in init
#a. name ="Vivalarazza"
#print(a.name)

# __repr__ is automatically called when any object is typcasted/ converted into a string
# It can be either print(str(a)) or print(a). Because print by default tries to convert into str
print(str(a))


# Class variables

class Student:
	counter = 1
	def __init__(self, name, grade):
		self.name = name
		#self.roll = 1 
		# So we can change the roll as counter and increment is whenever an object is created
		self.roll = Student.counter
		# And incrementing here
		Student.counter +=1
		self.grade = grade

	def __repr__(self):
		return f'Hi. My name is {self.name}, my roll number is {self.roll}, and my grade is {self.grade}'

# Here we will get the same roll no. for all the students. i.e 2. Hence to increase it one by one automatically whenever an object is created, we have to create a class variable
# Class variables can be accessed by class.variable. E.g Student.counter
obj1 = Student('Venkatesh', 'A')
print(obj1)
obj2 = Student('Radha', 'B')
print(obj2)
obj3 = Student('Raju', 'A')
print(obj3)


l = [x for x in range(10)]
print('This is l', l)