class Jar:
    def __init__(self, capacity=12,size=0):
      self.capacity = capacity
      if self.size > capacity:
        raise ValueError()
      self.size = size
      
      

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
      if n > self.capacity - self.size:
        raise ValueError("exceed the cookie jar’s capacity")
      self.size = self.size + n
      return(self.size)

    def withdraw(self, n):
      if n > self.size:
        raise ValueError('no enough cookies')
      self.size = self.size - n
      return(self.size)

    @property
    # Getter
    def capacity(self):
        return self._capacity
    # Setter
    @capacity.setter
    def capacity(self,capacity):
      if  int(capacity) < 0 :
        raise ValueError("Invalid Capacity")
      self._capacity = capacity

    # @property
    # # Getter
    # def size(self):
    #   return self.__size
    # @size.setter
    # def size(self,size):
    #   ...
    
    
    
def main():
  
  ...
  jar = Jar()
  # jar.deposit(12)
  # jar.withdraw(13)
  
  
  
  print(jar)
  
if __name__ == "__main__":
  main()

