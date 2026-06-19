def recalculate(student):

    student.total = (
        student.marks1 +
        student.marks2 +
        student.marks3 +
        student.marks4
    )

    student.total_avg = student.total / 4

    if student.total_avg >= 90:
        student.Grade = "Grade A"

    elif student.total_avg >= 80:
        student.Grade = "Grade B"

    elif student.total_avg >= 70:
        student.Grade = "Grade C"
        
    elif student.total_avg >= 50:
        student.Grade = "Grade D"

    else:
        student.Grade = "Fail"

    student.save()