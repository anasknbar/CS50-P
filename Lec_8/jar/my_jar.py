class Jar:
  def __init__(self,capacity=12,size=0):
    # if size > capacity or size < 0:
    #     raise ValueError("invalid size")
    
    
    self.capacity = capacity
    self.size = size
    
  def __str__(self):
    return self.size 
  
  def deposit(self,n):
    if n < 0 or n > self.capacity:
      raise ValueError("Invalid deposit")
    self.size += n
    
  def withdraw(self,n):
    if n < 0 or n > self.size:
      raise ValueError("Invalid withdraw") 
    self.size -= n  

  # Getter
  @property
  def capacity(self):
    return self._capacity
  
  # Setter
  @capacity.setter
  def capacity(self,capacity):
    if capacity < 0 :
      raise ValueError('Invalid capacity')
    self._capacity = capacity

  # Getter
  @property
  def size(self):
    return self._size 
  
  # Setter
  @size.setter
  def size(self,size):
    if size > self.capacity or size < 0:
      raise ValueError("invalid size")
    self._size = size
    
    
def main():
  jar = Jar()
  # jar.deposit(15)
  # jar.size = 20
  # jar.capacity = -1
  # jar.withdraw(50)
  # print(jar.capacity)
  print(jar)
  
  
if __name__ == "__main__":
  main()  