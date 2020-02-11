import json
import Professor
import TA
import Student


class System():

    def __init__(self):
        self.load_data()

    def load_data(self):
        self.users = self.load_user_db()
        self.courses = self.load_course_db()

    def load_user_db(self):
        with open('Data/users.json') as f:
            data = json.load(f)
        return data

    def load_course_db(self):
        with open('Data/courses.json') as f:
            data = json.load(f)
        return data

    def login(self,name, password):
        if self.check_password(name,password):
            role = self.users[name]['role']
            if role == 'professor':
                self.usr = Professor.Professor(name, self.users, self.courses)
            elif role == 'ta':
                self.usr = TA.TA(name, self.users, self.courses)
            elif role == 'student':
                self.usr = Student.Student(name, self.users, self.courses)

    def check_password(self, name, passwordEntered):
        password = self.users[name]['password']
        if passwordEntered == password:
            return True
        else:
            return False



if __name__ == "__main__":
    gradeSystem = System()
    gradeSystem.login('akend3', '123454321')
    gradeSystem.usr.submit_assignment('comp_sci','assignment1','Testing submit','1/1/20')

