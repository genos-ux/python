class Person:

    def __init__(self,name,age,gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("I go by the name ",self.name,",",self.age,"years of age","and I am a",self.gender)

student = Person('Gabriel',20,'male')
student.introduce()
