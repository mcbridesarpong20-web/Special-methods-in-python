#1.__init__() It is a constructor in python. It runs automatically when an instance of a class is created.
#It intializes the attributes of the object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Usage
student = Student("John", 20)
print(student.name) # Output: John 
print(student.age)  # Output: 20


#2. __str__() and __repr__() It is a special method in python that is used to return a string representation of an object. It is called when the str() function is called on an object.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Student('{self.name}', {self.age})"

#Usage
student = Student("John", 20)
print(student)  # Output: Student: John, Age: 20
print(repr(student))  # Output: Student('John', 20)


#3. __len__() It is a special method in python that is used to return the length of an object. It is called when the len() function is called on an object.
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

#Usage
my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # Output: 5

#4. __getitem__() It is a special method in python that is used to get an item from an object. It is called when the indexing operator [] is used on an object.
class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

#Usage
my_list = MyList([1, 2, 3, 4, 5])
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3


#5. __setitem__() It is a special method in python that is used to set an item in an object. It is called when the indexing operator [] is used on an object.
class MyList:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, index, value):
        self.items[index] = value

#Usage
my_list = MyList([1, 2, 3, 4, 5])
my_list[1] = 10
print(my_list.items)  # Output: [1, 10, 3, 4, 5]

#6. __eq__() It is a special method in python that is used to compare two objects for equality. It is called when the == operator is used on an object.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
            return self.name == other.name and self.age == other.age
    
#Usage
student1 = Student("John", 20)      
student2 = Student("John", 20)
print(student1 == student2)  # Output: True

#7. __add__(), __sub__() and __mul__() It is a special method in python that is used to add, subtract, or multiply two objects. It is called when the +, -, or * operator is used on an object.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

#Usage
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
vector3 = vector1 + vector2
vector4 = vector1 - vector2
vector5 = vector1 * 2
print(vector3.x, vector3.y)  # Output: 4 6
print(vector4.x, vector4.y)  # Output: -2 -2
print(vector5.x, vector5.y)  # Output: 2 4

#8. __call__() It is a special method in python that is used to make an object callable. It is called when the object is called as a function.
class MyClass:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"My name is {self.name}")

#Usage
my_object = MyClass("John")
my_object()  # Output: My name is John

#9. __del__() It is a special method in python that is used to delete an object. It is called when the object is deleted using the del statement.
class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is being deleted")

#Usage
my_object = MyClass("John")
del my_object  # Output: John is being deleted

#10. __contains__() It is a special method in python that is used to check if an object contains a specific item. It is called when the in operator is used on an object.
class MyList:   
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

#Usage
my_list = MyList([1, 2, 3, 4, 5])
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False

#11. __iter__() and __next__() It is a special method in python that is used to make an object iterable. It is called when the iter() function is called on an object.
class MyList:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
        
#Usage
my_list = MyList([1, 2, 3, 4, 5])
for item in my_list:
    print(item)  # Output: 1 2 3 4 5

#12. __bool__() It is a special method in python that is used to return the boolean value of an object. It is called when the bool() function is called on an object.
class MyClass:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return bool(self.value)
    
#Usage
my_object1 = MyClass(0)
my_object2 = MyClass(10)
print(bool(my_object1))  # Output: False
print(bool(my_object2))  # Output: True