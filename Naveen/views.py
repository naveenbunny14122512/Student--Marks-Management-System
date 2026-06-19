from .models import Student
from .utils import recalculate
from django.shortcuts import render, redirect

def SRS(request):
    
    if request.method == 'POST':

        name = request.POST.get('Name') 
        m1 = request.POST.get('marks1')
        m2 = request.POST.get('marks2')
        m3 = request.POST.get('marks3')
        m4 = request.POST.get('marks4')

        # storing old values for UI refill
        context = {
            "Name": name,
            "m1": m1,
            "m2": m2,
            "m3": m3,
            "m4": m4,
        }

        # validations
        if not name:
            context["Error"] = "Please Enter Your Name"
            return render(request, "1412.html", context)

        if not m1:
            context["Error"] = "Please Enter 1st Subject Marks"
            return render(request, "1412.html", context)

        if not m2:
            context["Error"] = "Please Enter 2nd Subject Marks"
            return render(request, "1412.html", context)

        if not m3:
            context["Error"] = "Please Enter 3rd Subject Marks"
            return render(request, "1412.html", context)

        if not m4:
            context["Error"] = "Please Enter 4th Subject Marks"
            return render(request, "1412.html", context)

        marks = [
            int(m1),
            int(m2),
            int(m3),
            int(m4)
        ]

        total = sum(marks)
        total_avg = total / len(marks)

        # grading
        if total_avg >= 90:
            grade = "Grade A"

        elif total_avg >= 80:
            grade = "Grade B"

        elif total_avg >= 70:
            grade = "Grade C"

        elif total_avg >= 50:
            grade = "Grade D"

        else:
            grade = "Fail"
            
        Student.objects.create(
            Name=name,
            marks1=marks[0],
            marks2=marks[1],
            marks3=marks[2],
            marks4=marks[3],
            total=total,
            total_avg=total_avg,
            Grade=grade
        )
            

        # final result
        context.update({
            "Grade": grade,
            "total": total,
            "total_avg": total_avg 
        })

        return render(request, "1412.html", context)

    return render(request, "1412.html")



def view_students(request):

    students = Student.objects.all()
    return render(request,"view_students.html",{ "students": students}
    )


def update_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.Name = request.POST.get("Name")
        student.marks1 = int(request.POST.get("marks1"))
        student.marks2 = int(request.POST.get("marks2"))
        student.marks3 = int(request.POST.get("marks3"))
        student.marks4 = int(request.POST.get("marks4"))

        recalculate(student)

        return redirect('/view/')

    return render(request,"update_student.html",{"student": student})

def delete_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.delete()

        return redirect('view_students')

    return render(request,"confirm_delete.html",{"student": student})



        
        
        
            
            
    