import datetime
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
            
    @classmethod
    def get_age_from_year(cls,name,year):
        age=datetime.datetime.now().year -year
        return cls(name,age)


p1 = Person("Alam",22)
print(p1.name)
p2 = Person.get_age_from_year("Bimal",2005)
print(p2.name, p2.age)



