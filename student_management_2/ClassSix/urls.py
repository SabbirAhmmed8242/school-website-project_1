from django.urls import path,include
from . import views

urlpatterns = [
    path ('',views.classSIx, name='ClassSixHome'),



    path ('student/join',views.StudentReg, name='StudentReg'),
    path ('student/login/',views.StudentLogin, name='StudentLogin'),
    path ('student/logout/',views.StudentLogOut, name='StudentLogOut'),
    path ('student/dashbord/',views.StudentDashbord, name='ClassSixStudentDashbord'),
    path ('student/marksheet/',views.student_marksheet, name='marksheet'),
    path ('student/viewResult/',views.ClassSixStudentResultView, name='AllResultSix'),


    
    path ('teacher/Join/',views.TeaccherReg, name='TeacherRegSIX'),
    path ('teacher/login/',views.TeacherLogin, name='TeacherLoginSIX'),
    path ('teacher/logout/',views.TeacherLogOut, name='TeacherLogOut'),
    path ('teacher/AddResult/',views.ClassSixRslt, name='Addresult'),
    path ('teacher/dashboard/',views.ClassSixTeacgerDashbord, name='ClassSixTeacgerDashbord'),
    
]