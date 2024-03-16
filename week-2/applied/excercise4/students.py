""" 
    Create an abstract class Student that will be used for Monash University. 
    Think about what kind of variables you want to make as class variables 
    and instance variables. 
"""

from abc import ABC, abstractmethod

class Student(ABC):
    
    def __init__(self, name, campus):
        self.name = name
        self.campus = None

class ClaytonStudent(Student): 
    
    def __init__(self, course):
        Student.__init(self)
        
        self.course = course
        self.campus = "Clayton"

class MalaysiaStudent(Student):
    
    def __init__(self, course):
        Student.__init__(self)
        
        self.course = course
        self.campus = "Malaysia"