from django.shortcuts import render,redirect
from . models import SixStudentID, ClassSIXResult , ClassSixTeachers
from django.contrib.auth.hashers import make_password , check_password

def classSIx(request):
    return render(request, 'ClassSixHomePage.html')

def StudentReg(request):
    if request.method=="POST":
        name =request.POST.get('name')
        FatherName = request.POST.get('FatherName')
        MotherName = request.POST.get('MotherName')
        roll = request.POST.get('roll')
        StudentId = int(request.POST.get('StudentID'))
        password = request.POST.get('password')
        con_password = request.POST.get('con_pasword')

        if password == con_password:
            hashed_password = make_password(password)
            NewStudent = SixStudentID.objects.create(
                name= name , FatherName = FatherName , MotherName= MotherName,
                roll = roll , StudentID = StudentId , password = hashed_password
            )
            NewStudent.save()
            return redirect('StudentLogin')
        else:
            err = 'password didnot match'
            return render(request , 'StudentReg.html',{'err':err})
    return render(request, 'StudentReg.html')



def StudentLogin(request):
    if request.method == 'POST':
        StudentID = request.POST.get('StudentId')
        password = request.POST.get('password')
        try:
            Student = SixStudentID.objects.get(StudentID = StudentID)
            if check_password(password, Student.password):
                request.session['student_id'] = Student.id
                return redirect('ClassSixStudentDashbord')
            else:
                err = 'Password DidNot Match'
                return render(request, 'Studentlogin.html',{'err':err})
        except:
            err = "Student Id not exsits"
            return render(request, 'Studentlogin.html', {'err':err}) 
    return render(request, 'Studentlogin.html')

from django.shortcuts import render, get_object_or_404

def student_marksheet(request):
    if request.method == 'POST':
        studentID = request.POST.get('StudentId')
        try:
            student = ClassSIXResult.objects.get(student_id=studentID)
            context = {'student': student}
            return render(request, 'marksheet.html', context)
        except ClassSIXResult.DoesNotExist:
            err = "Student ID not found"
            return render(request, 'marksheetForm.html', {'err': err})

    return render(request, 'marksheetForm.html')


def ClassSixStudentResultView(request):
    results = ClassSIXResult.objects.all()
    return render(request, 'ClassSixStudentResults.html', {'results':results})
    

def StudentLogOut(request):
    try: 
        del request.session['student_id']
    except TypeError:
        pass
    return redirect('StudentLogin')


def StudentDashbord(request):
    return render(request, 'ClassSixStudentDashbord.html')

    
def TeaccherReg(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        NID = int(request.POST.get('NID'))
        password = request.POST.get('password')
        con_pass = request.POST.get('con_pass')

        if password == con_pass:
            hashedPass = make_password(password)
            NewTeacher = ClassSixTeachers.objects.create(
                name = name , username = username , NID = NID,
                password = hashedPass
            )
            NewTeacher.save()
            return redirect('TeacherLoginSIX')
        else:
            err = "Password Did not match"
            return render(request , 'teacherreg.html' , {'err':err})
    return render(request , 'teacherreg.html')



def TeacherLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        TeacherOf = request.POST.get('classes')

        if str(TeacherOf).lower() in ['six' , 6]:
            teacher = ClassSixTeachers.objects.get(username = username)
            if check_password(password , teacher.password):
                request.session['teacher_id'] = teacher.id
                return redirect('ClassSixTeacgerDashbord')
            else:
                err = 'password did not match'
                return render(request , 'Teacherlogin.html', {'err':err})
        else:
            err = 'input err'
            return render(request , 'Teacherlogin.html',{'err':err})
    return render(request, 'Teacherlogin.html')

def ClassSixTeacgerDashbord(request):
    return render(request, 'ClassSixTeacgerDashbord.html')



def TeacherLogOut(request):
    try:
        del request.session['teacher_id']
        return redirect('TeacherLoginSIX')
    except TypeError:
        return redirect('TeacherLogin')



def ClassSixRslt(request):
    if not request.session.get('teacher_id'):
        return redirect('TeacherLogin')
    
    if request.method == "POST":
        name = request.POST.get('name')
        roll = int(request.POST.get('roll'))
        studentID = int(request.POST.get('StudentId'))
        FatherName = request.POST.get('FatherName')

        bangla = float(request.POST.get('bangla'))
        english = float(request.POST.get('english'))
        math = float(request.POST.get('math'))
        biology = float(request.POST.get('biology'))
        chemistry = float(request.POST.get('chemistry'))
        physics = float(request.POST.get('physics'))

        total = bangla + english + math + biology + chemistry + physics
        avarage = total/6

        if bangla <= 100 and english <= 100 and math <= 100 and biology <= 100 and chemistry <= 100 and physics <= 100:
            result = ClassSIXResult.objects.create(
                name = name , roll = roll , student_id = studentID , FatherName =FatherName,
                bangla = bangla , english =english , math = math , biology = biology , chemistry = chemistry , physics=physics,
                total =total, avarage =avarage
            )
            result.save()
            succes = 'Result Add succesfully'
            return render(request , 'AddStudentResult.html',{'succes':succes})
        else:
            err = 'input err'
            return render(request , 'AddStudentResult.html',{'err':err})
    return render(request , 'AddStudentResult.html')


# Create your views here.
