from django.contrib import admin
from lessons.models import *



class StudentAdmin(admin.ModelAdmin):
	list_display = ('student',)

	def student(self, obj):
		return obj.Student.student

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'start_time', 'finish_time')
	search_fields = ('title', 'start_time', 'finish_time')
	list_filter = ('title', 'start_time')


class InstructorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email','phone','course')
	search_fields = ('first_name', 'last_name', 'email', 'course')
	list_filter = ('course', 'email')

class LessonAdmin(admin.ModelAdmin):
	list_display = ('lesson_title','course', 'instructor','published_date')
	search_fields = ('lesson_title', 'lesson_body', 'instructor')
	list_filter = ('instructor',)
	list_per_page = 10

	def course(self, obj):
		return obj.instructor.course

	def instructor(self, obj):
		return obj.instructor.first_name

admin.site.site_header = "Abdoulthegreat Admin"
admin.site.site_title = "Abdul Admin Portal"
admin.site.index_title = "Welcome to Abdoulthegreat Portal"

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)