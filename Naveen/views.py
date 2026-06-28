from django.http import HttpResponse

from .models import Student
from .utils import recalculate
from django.shortcuts import render, redirect
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username and password:
            user=auth.authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Invalid username or password.')
                return redirect('login')
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')   
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if FirstName and LastName and Email and username and password and confirm_password:
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exists.')
                    return redirect('register')
                
                elif User.objects.filter(email=Email).exists():
                    messages.info(request, 'Email already exists.')
                    return redirect('register')
                
                else:
                    User.objects.create_user(
                        first_name=FirstName,
                        last_name=LastName,
                        email=Email,
                        username=username,
                        password=password
                    )
                    messages.info(request, 'Registration successful. You can now log in.')
                    return redirect('login')
            else:
                error_message = "Passwords do not match."
                messages.info(request, error_message)
                return redirect('register')

            
    else: 
        return render(request, "register.html")
    
def verify_password(request):
    if request.method=="POST":
        password=request.POST.get("password")
        user=auth.authenticate(request, username=request.user.username, password=password)
        if user is not None:
            return redirect('view_students')  # Replace 'view_students' with the actual URL name for your view students view
        else:
            messages.info(request, 'Incorrect password.')
            return render(request, "verify.html")
    else:
        return render(request,"verify.html")
    
@login_required
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


@login_required
def view_students(request):

    students = Student.objects.all()
    return render(request,"view_students.html",{ "students": students}
    )

@login_required
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

@login_required
def delete_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.delete()
        return redirect('view_students')
    return render(request,"confirm_delete.html",{"student": student})



        
        
        
            
            
    