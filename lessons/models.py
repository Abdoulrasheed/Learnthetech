from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
	title = models.CharField(max_length=50)
	course_description = models.TextField(max_length=500, blank=True, null=True)
	start_time = models.DateTimeField(auto_now_add=False)
	finish_time = models.DateTimeField(auto_now_add=False)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

class Instructor(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(blank=True, null=True)
	twitter_handler = models.CharField(max_length=50, blank=True, null=True)
	facebook_id = models.CharField(max_length=50, blank=True, null=True)
	pinterest = models.CharField(max_length=50, blank=True, null=True)
	google_plus = models.CharField(max_length=50, blank=True, null=True)
	position = models.CharField(max_length=30, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name + " " + self.last_name

class Student(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	course_enrolled = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return self.student.first_name

class Lesson(models.Model):
	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	lesson_title = models.CharField(max_length=200, blank=True, null=True)
	lesson_body = models.TextField(blank=True, null=True)
	published_date = models.DateTimeField(auto_now_add=True	)

	def __str__(self):
		return self.lesson_title