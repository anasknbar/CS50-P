    class Student:
      ...
    def main():
      student = get_name()
      print(f"{student.name} live in {student.house}")
      
      
    def get_name():
      student = Student()
      student.name = input("Name: ")
      student.house = input("House: ")
      return student

    if __name__ == "__main__":
      main()

- In Python, when you write student = Student(), you are creating an instance of the Student class. This instance is an object in memory that has been initialized based on the definition of the Student class.

In this case:

  ### student 
  is a variable name that refers to the newly created instance of the Student class.
  This instance represents a specific student in your program.
  By calling Student(), you are invoking the constructor method __init__() of the Student class to initialize the instance.
  Any attributes or methods defined within the Student class can be accessed through this instance using dot notation.

For example, after student = Student(), you can access the name attribute of the student instance using student.name, and you can access the house attribute using student.house.

In object-oriented programming, instances of classes are often referred to as objects. So, student is an object of the Student class. Each instance of a class represents a unique object with its own set of attributes and methods.