""" Week 2 Excercise 2

    In excercise2.py define a new class AthleteWorker that uses inheritance to combine
    the attributse of a worker and an athlete and defines appropriate __init__
    and __str__ methods. Additionally, extend the Person class with an __eq__
    method that considers two people equivalent if they have the same passport.
    
    In excercise.txt discuss how could this be used in your AthleteWorker class
    to determine wheter two such objects are equivalent.
    
"""

class Person:
    def __init__(self , name: str, surname: str, passport: str) -> None:
        self.name = name
        self.surname = surname
        self.passport = passport
        
    def __eq__(self , other) -> bool:
        return isinstance(other ,Person) and self.passport == other.passport
        
    def __str__(self) -> str:
        return self.name + ", " + self.surname + ", " + str(self.passport)

class Worker(Person):
    def __init__(self , name: str, surname: str, passport: str, job: str) -> None:
        Person.__init__(self , name , surname , passport)
        self.job = job
        
    def __str__(self) -> str:
        return Person.__str__(self) + ", " + str(self.job)

class Athlete(Person):
    def __init__(self , name: str, surname: str, passport: str, sport: str) -> None:
        Person.__init__(self , name , surname , passport)
        self.sport = sport
    def __str__(self) -> str:
        return Person.__str__(self) + ", " + str(self.sport)
    
class AthelteWorker(Athlete, Worker):
    def __init__(self, name, surname, passport, job, sport):
        Worker.__init__(self, name, surname, passport, job)
        Athlete.__init__(self, name, surname, passport, job, sport)
        
    def __str__(self) -> str:
        return Athlete.__str__(self) + ", " + str(self.job)