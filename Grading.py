# we have a dicr=tionary and for each value we need to check if : 
# 1-  grade bettwen 91 - 100 we have to print "Outstanding"
# 2- grade bettwen 81 - 90 we have to print "Exceeds Expectations" 
# 3- grade bettwen 71- 80 we have to print "Acceptable"
# 4- grade below 70 we have to print "Fail"

students_grades={"Harry":91,"Mike":78,"Ran":50,"Lisa":"98","Anna":67}

students_rate={}
for stu in students_grades:
    grade= int(students_grades[stu])
    if grade > 90:
        students_rate[stu] = "Outstanding"
    elif grade > 80 :
        students_rate[stu]="Exceeds Expectations"
    elif grade > 70 :
        students_rate[stu]="Acceptable"
    else:
        students_rate[stu]="Fail"

print(students_rate)