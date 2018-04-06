# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from lessons.forms import SignUpForm
from lessons.models import Student, Instructor, Lesson, Course
from django.shortcuts import get_object_or_404

@login_required
def course_list(request):
    courses = Course.objects.all().order_by('-start_time')
    ins = Instructor.objects.all()
    stud = User.objects.all()

    c_students = stud.count()
    c_staff = ins.count()
    c_courses = courses.count()
    return render(request, 'lesson/courses.html', {'courses': courses, 'c_courses': c_courses, 'c_students': c_students, 'c_staff': c_staff, 'instructor': ins[0] })


@login_required
def course_read(request, pk):
    lessons = Lesson.objects.filter(instructor_id = pk).order_by('-instructor_id')
    if lessons:
        return render(request, 'lesson/course_read.html', {'lessons': lessons, 'l':lessons[0]})
    else:
        return render(request, 'lesson/course_read.html', {'lessons': lessons, 'info': 'there are no lessons published yet'})

@login_required
def services(request):
    instructors = Instructor.objects.all()
    return render(request, 'lesson/services.html', {'instructors': instructors })


def signup(request):
    instructors = Instructor.objects.all()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('course_list')
    else:
        form = SignUpForm()
    return render(request, 'lesson/signup.html', {'form': form, 'instructors': instructors})
