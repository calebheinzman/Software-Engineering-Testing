import User

class Student(User.User):
    def __init__(self, name,users,courses):
        self.users = users
        self.all_courses = courses
        self.name = name
        self.courses = self.users[name]['courses']
        self.password = self.users[name]['password']

    def submit_assignment(self,course,assignment_name,submission,submission_date):
        due_date = self.all_courses[course]['assignments'][assignment_name]["due_date"]
        submission = {assignment_name: {
          "grade": 'N/A',
          "submission_date": submission_date,
          "submission": submission,
            "ontime": self.check_ontime(submission_date,due_date)
        }}
        self.users[self.name]['courses'][course].update(submission)
        self.update_user_db()

    def check_ontime(self,submission_date,due_date):
        return True

