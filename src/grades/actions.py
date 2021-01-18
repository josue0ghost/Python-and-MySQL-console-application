import grades.grade as gradeModel

class Actions:

    def create(self, user):
        title = input("Grade title: ")
        description = input("Grade description: ")

        newGrade = gradeModel.Grade(user[0], title, description)
        save = newGrade.save()

        if save[0] >= 1:
            print(f"Grade has been registered as: {newGrade.title}")
        else:
            print(f"Grade registration failed")
    
    def show(self, user):
        print(f"Showing {user[1]} grades")
        gradeData = gradeModel.Grade(user[0], "", "")
        gradeList = gradeData.select()

        for grade in gradeList:
            print("--------------------------")
            print(f"Title: {grade[2]}")
            print(f"Description: {grade[3]}")
    
    def delete(self, user):
        print(f"Delete {user[1]} grades where title contains...")
        title = input("Title: ")

        grade = gradeModel.Grade(user[0], title, "")
        gradeDelete = grade.delete()

        if gradeDelete[0] >= 1:
            print(f"Grade {gradeDelete[1].title} has been deleted")
        else:
            print("Grade delete failed")

            