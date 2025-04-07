from django.shortcuts import render,redirect


def home(request):
    return render(request,'Home.html')


def TeacherLoginClass(request):
    return render(request , "TeacherLoginClass.html")