class vehicle: #parent class
    def __init__(self,name,maxspeed,mileage):
      self.name = name
      self.maxspeed = maxspeed
      self.mileage = mileage

class bus(vehicle): #child class inherited from parent class
  def __init__(self,name,maxspeed,mileage,color):
     self.color = color
     vehicle.__init__(self,name,maxspeed,mileage)

     
#object creation
v1 = bus("tesla", "i don't know", 55, "White")
print("Tasheen's fav color is:",v1.color)
print("Tasheen's fav car is:",v1.name)

v2 = bus("BMW", "i don't know", 45, "Green")
print("Vedanshi's fav car is:",v2.name)
print("Vedanshi's fav color is:",v2.color)