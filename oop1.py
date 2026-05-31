class Dog:
  species = "Dog"
  def __init__(self, name, age):
    self.name= name
    self.age= age

Nelson = Dog("Nelson", 8)

Bruno = Dog("Bruno", 10)
print("Nelson Is A {} " .format(Nelson.species))
print("Bruno Is Also A {}" .format(Bruno.species))
print("Nelson Is {}" .format(Nelson.age) ,"Years Old" )
print("{} Is {} Years Old" .format(Bruno.name , Bruno.age))