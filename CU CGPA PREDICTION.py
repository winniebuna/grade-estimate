# CGPA CALCULATOR FOR THAT SEMESTER
# float GP,CU, PS,TGP,TCU,GPA,CGPA
listcourse = []
listgrade = []
listgradepoint = []
listcredit = []
list_all_gpa = []
list_all_tcu = []
list_all_tgp = []
# A COUNT VARIABLE IS GOING TO COME HERE TO LOOP THE COURSE FOR HOW MANY COURSES YOU OFFER FOR THAT SEMESTER

print('welcome to CGPA predictor, lets predict your next CGPA')
current_cgpa = float(input('first enter your current CGPA : '))
print('Great! now lets begin ')
numcourse = int(input('how many courses will you take in the semester ? '))
count = 0
while count < numcourse:

    course_name = input('enter course name: ')
    credit_unit = int(input('enter credit unit for this couse : '))
    point_score = int(input('enter point score for this course : '))
    grade_point = credit_unit * point_score
    # A METHOD COMES IN HERE TO CALCULATE AND GIVE OUT THE GRADE OF THE STUDENT BUT STORES THE VALUE IN A DICTIONARY
    def whatsmygrade(x):
        if x == 5:
            print('GRADE : A')
            listgrade.append('A')
        elif x == 4:
            print('GRADE : B')
            listgrade.append('B')
        elif x == 3:
            print('GRADE : C')
            listgrade.append('C')
        elif x == 2:
            print('GRADE : D')
            listgrade.append('D')
        elif x == 0:
            print('GRADE : F')
            listgrade.append('F')
        else:
            print('ENTER A VALID POINT SCORE')

    whatsmygrade(point_score)
    listcourse.append(course_name)
    listcredit.append(credit_unit)
    listgradepoint.append(grade_point)
    # A METHOD COMES IN HERE TO CHECK IF THE COURSE ENTERED ALREADY BELONGS IN THE DICTIONARY; TO AVOID DOUBLE ENTRY
    count += 1
print(listcourse, listgradepoint, listgrade)
TGP = sum(listgradepoint)
TCU = sum(listcredit)
print(TGP)
print(TCU)
GPA = TGP/TCU
print('Your GPA for this semester is : ', GPA)
print('now lets predict your CGPA for next semester')
semesters = int(input('how many semesters have you completed ? '))
semester_count = 0
list_total_tcu = []
list_total_tgp = []
while semester_count < semesters:
    list_total_tcu.append(int(input('enter total credit unit for each semester completed : ')))
    list_total_tgp.append(int(input('enter total point score for that semester : ')))
    semester_count += 1
STGP = sum(list_total_tgp)
print(STGP)
STCU = sum(list_total_tcu)
print(STCU)
CGPA = (TGP + STGP) / (TCU + STCU)
print('This means that if you get ', GPA, ' GPA in this coming semester, your new CGPA will be : ', CGPA)
print('GOODLUCK REACHING YOUR GOAL FOR NEXT SEMESTER !!')
print(' :) ')

