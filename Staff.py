import json
import User

class Staff(User.User):

    def update_course_db(self):
        with open('Data/courses.json', 'w') as fp:
            json.dump(self.all_courses, fp)

    def createAssignment(self,assignment_name, due_date, course):
        assignment = {
            assignment_name: {
                'due_date': due_date
            }
        }
        self.all_courses[course]['assignments'].update(assignment)
        self.update_course_db()

    def changeGrade(self,user,course,assignment,grade):
        self.users[user]['courses'][course][assignment]['grade'] = grade
        self.update_user_db()

