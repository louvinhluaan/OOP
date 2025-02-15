from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, major, student_id):
        self.name = name
        self.major = major
        self.id = student_id
    
    @abstractmethod
    def get_profile(self):
        pass

class FullTimeStudent(Student):
    def __init__(self, name, major, student_id, project=None):
        super().__init__(name, major, student_id)
        self.joined_project = project
        self.research_profile = ""

    def get_profile(self):
        return self._research_profile
    
# Problem 2
class PartTimeStudent(Student):
    count = 0
    
    def __init__(self, name, major, student_id, min_hour=0, max_hour=0):
        super().__init__(name, major, student_id)
        self.min_hour = min_hour
        self.max_hour = max_hour
        PartTimeStudent.count += 1

    @staticmethod
    def get_count():
        return PartTimeStudent.count

class Lecturer:
    def __init__(self, lecturer_id, name, rank):
        self.id = lecturer_id
        self.name = name
        self.rank = rank
        self.project_led = None
        self.joined_projects = []
        self.research_profile = ""
    
class Project:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.leader = None
        self.members = []

# Problem 3
class SchoolSystem:
    def __init__(self):
        self.students = []
        self.lecturers = []
        self.projects = []
    
    def add_student(self, student):
        if len(self.students) < 10:
            self.students.append(student)
        else:
            print("Can not add more students, limit reached.")
    
    def add_lecturer(self, lecturer):
        if len(self.lecturers) < 10:
            self.lecturers.append(lecturer)
        else:
            print("Can not add more lecturers, limit reached.")
    
    def add_project(self, project):
        if len(self.projects) < 10:
            self.projects.append(project)
        else:
            print("Can not add more projects, limit reached.")