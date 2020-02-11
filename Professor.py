import json
import Staff


class Professor(Staff.Staff):
    def __init__(self, name,users,courses):
        self.users = users
        self.all_courses = courses
        self.name = name
        self.courses = self.users[name]['courses']
        self.password = self.users[name]['password']




