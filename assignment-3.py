"""
Day 4
Turkish Ai Hub - Assignment 3
@author: Mehmet Baran Munar
"""

# just for fun 
from emoji import emojize

studentInformations = dict()

# Ask the user for student names and grades.
# adding those to dictionary and return it.
def studentInformation():
    student = dict()
    name = input("Please enter student's name.")
    midterm = float(input("Please enter midterm grade."))
    project = float(input("Please enter project grade."))
    final = float(input("Please enter final grade."))
    grades = [midterm,project,final]
    student["Name"] = name
    student["Grades"] = grades
    return student

# Adding all students to dictionary.
def addStudentInformations():
    # it should be 5 student.
    for x in range(1,6):
        try:
            studentInformations[f"Student {x}"] = studentInformation()
            x += 1
        except ValueError:
            print("!!!Please enter grade with integer or float values.")
            break
    return studentInformations

# All informations about students.(names and grades)
print("All student informations so far:",addStudentInformations())

# list of average grades of all students.
meanGradeList = list()

# calculating student averages and appending these grades to a list.
def calculateAverages():
    for i in range(1,6):
        a = studentInformations[f"Student {i}"]["Grades"]
        meanGrade = (a[0]*0.3) + (a[1]*0.3) + (a[2]*0.4)
        # to avoid high decimal numbers.
        meanGrade = round(meanGrade, 2)
        meanGradeList.append(meanGrade)
try:
    calculateAverages()
    # sorting from bigger to smaller.
    # bigger comes first
    """ with function """
    # def sort_descending(list):
    #     list.sort(reverse=True)
    #     return list
    """ with lambda """
    sort_descending  = lambda list:sorted(list,reverse=True)
    print("Sorting averages via descending order:",sort_descending(meanGradeList))
except KeyError:
    print("!!!You need to enter integer or float values to calculate average.")
    print(emojize(":thumbs_down:Please run program again.:thumbs_down:"))

def bestGrade(*args):
    for i in args:
        print("Best grade is :",max(i))
        print("Worst grade is :",min(i))
bestGrade(meanGradeList)
