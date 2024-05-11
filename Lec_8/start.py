# -------------------------------------------(class method)--------------------------------------------------------------
# perviously we talk about method and variables as object/instance method and object/instance variables , yet another types is worth mentioning which is class method class variables.
# as it turns out that sometimes I need to associate a function or variables to the class(@classmethod) itself not with the object/instance as we periviously did
import random
class Hat:
  # this is a class variables that I can use any where in the class, notice there is no 'self' keyword
  cities = ['amman','irbid','zarqa'] 
  
  # using class method I do not need to instantiate any Hat object as previous. 
  @classmethod
  def sort(cls,name): # we replace self with cls which is a reference to the class itself.
    print(name,'is in',random.choice(cls.cities))
  

Hat.sort("Anas") # no need to instantiate anymore, I am using it as if it was a python class function like int,str..etc

# -------------------------------------------(Properties, Getters and Setters)-------------------------------------------
# class Student():
#   def __init__(self,name,city):
   
#     self.name = name
#     self.city = city # even thought i remove the checking error, python will still called the property once it see the assign symbol > [self.city =]
    
#   def your_own_method():
#     ...
    
#   def __str__(self):
#     return f"{self.name} live in {self.city}"
  
#   # Getter
#   @property
#   def name(self):
#     return self._name
  
#   # setter
#   @name.setter
#   def name(self,name):
#     if not name :
#       raise ValueError("missing name")
#     self._name = name 


#   @property
#   def city(self):
#     return self._city
#   @city.setter
#   def city(self,city):
#     if city not in ['amman','irbid']:
#       raise ValueError("wrong city")
#     self._city = city
#   # unfortinutely, If I have an instance variable called city(as in the __init__) I can not have also a function called city as in the Getter/Setter function. So the conventional fix for this is to put underscore _ to distinguish between the instance variables and the function
#   ...
 
 
# def main():
#   student = get_name()
#   # here I circumvent the Student class error checking, now damascus will not show valueError!!. using the dot notation as we start at the begining I can re-assign the city and pass the Student rasing error. because the error checking nly called once we create the Student object/instance. How to prevent this? >> properties
#   # In Python, properties in a class refer to attributes of the class that have getter, setter, and deleter methods associated with them. They allow you to define custom behavior when accessing, setting, or deleting an attribute of an object.
#   # Properties are useful when you want to control access to attributes, validate input, or execute some code whenever an attribute is accessed, set, or deleted.
#   student.name = '' # python will call the @property automatically on this line. How?? 
#   print(student)

# def get_name():
#   name = input("Name: ")
#   city = input("City: ")

#   return Student(name,city)
 

# if __name__ == "__main__":
#   main()










# -------------------------------------------(Instance Methods)----------------------------------------------------------
# # create a class
# # addition to instance variable (name,house), you can add instance method (function),
# # Dunder __init__ method it's standard method used to initialize the content of an object from a class
# class Student(): 
#   def __init__(self,name,city): 
#     if not name :
#       raise ValueError("missing name")
#     if city not in ['irbid','amman','zarqa']:
#       raise ValueError("wrong city")
#     self.name = name # we added instance varibles to this object/instance as previous, but from the class itself 
#     self.city = city
#     ...
#   # Dunder __str__ method, its a special method that if you defined inside of your class Python will just automatically call this function any time some other function wants to see your object/instance as a string (print). checkout __repr__ method
#   def __str__(self):
#     return f"{self.name} from {self.city}"

# def main():
#   student = get_name()
#   print(student) # I only used student, because I use __str__ method in the Student class.
  
  
# def get_name():
#   name = input("Name: ")
#   city = input("City: ")
#   try:
#     student = Student(name,city) # instantiate a student object/instance and passing argument to the class function which will evoke a constructor call always to the __init__ function by definition > you can return Student(name,house)
#     return student
#   except ValueError:
#     ...
  

# if __name__ == "__main__":
#   main()






















# -------------------------------------------(intro)---------------------------------------------------------------------
# class Student: # here I am creating a class, which enable me to create a custom data type
#   ...

# def main():
#   student = get_name()
#   print(f"{student.name} live in {student.house}")
  
  
# def get_name():
#   student = Student() # here I am using that class, creating what's called an object/instance (student) from that class, in techinical words, class is the definition of a new data type, the object is the instantiation of that class
#   student.name = input("Name: ")   # >> store attributes/instance variables in the new instance of class (object)
#   student.house = input("House: ") # >> store attributes/instance variables  in the new instance of class (object)
#   return student

# if __name__ == "__main__":
#   main()
  
