import random


class Person:

  def __init__(self,name,age):
#     print("my name is ",name)
     self.name = name
#  def __init__(self,age):
     self.age = age


  def introduce(self):
      print("-----------------------------")
      print("Your name is ",self.name)
      print("and You are ",self.age,"years old.")

  def count(self):
      x = self.age + 10
      print("-----------------------------")
      print("After 10 years, You will be ", x, " years old.")


yourname = input("what is your name?  ")
yourage = int(input("what is your age  "))

person1 = Person(yourname,yourage)

person1.introduce()
person1.count()
