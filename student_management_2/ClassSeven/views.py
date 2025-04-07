from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClassSevenResult ,ClassSevenStudentID ,ClassSevenTeachers
from django.contrib.auth.hashers import make_password , check_password
from django.views.decorators.cache import never_cache

def ClassSevenHome(request):
    return render(request,'ClassSevenHomePage.html' )


def ClassSevenStudentReg(request):
    if request.method == "POST":
        name = request.POST.get('name')
        FatherName = request.POST.get('FatherName')
        MotherName = request.POST.get('MotherName')
        StudentID =request.POST.get('StudentID')
        password = request.POST.get('password')
        con_password = request.POST.get('con_pasword')

        if password == con_password:
            HasedPass = make_password(password)
            NewStudent = ClassSevenStudentID.objects.create(
                name = name , FatherName = FatherName , MotherName = MotherName,
                StudentID = StudentID , password = HasedPass,
            )
            NewStudent.save()
            return redirect('ClassSevenStudentLogin')
        else:
            err = 'Password not match'
            return render(request , 'ClassSevenStudentReg.html',{'err':err})
    return render(request, 'ClassSevenStudentReg.html')

def ClassSevenStudentLogin(request):
    if request.method == "POST":
        StudentID = request.POST.get('StudentId')
        password = request.POST.get('password')
        
        try:
            Student = ClassSevenStudentID.objects.get(StudentID=StudentID)
            if check_password(password, Student.password):
                request.session['student_id'] = Student.id
                return redirect('ClassSevenStudentDashboard')
            else:
                err = 'Password did not match'
                return render(request, 'ClassSevenStudentLogin.html', {'err':err})
        except:
            err = "StudentID not found"
            render(request, 'ClassSevenStudentLogin.html',{'err':err})
    return render(request, 'ClassSevenStudentLogin.html')


def ClassSevenStudentLogOut(request):
    try: 
        del request.session['student_id']
        return redirect('ClassSevenStudentLogin')
    except TypeError:
        pass
    return render('ClassSevenStudentLogin')
# Create your views here.
