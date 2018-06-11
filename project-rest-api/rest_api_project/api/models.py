from django.db import models

# Create your models here.

class Course(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=True, default='')
	description = models.TextField()
	dept = models.CharField(max_length=100, blank=True, default='')
	course_code = models.CharField(max_length=100)
	
	def __str__(self):
			return "{}{}: {}".format(self.dept, self.course_code, self.name)

class Assesment(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200, blank=True, default='')
	description = models.TextField()
	due_date = models.DateTimeField()
	assgn_date = models.DateTimeField()

	def __str__(self):
		"""String rep of model."""
		return "{}: {}".format(self.title, self.description)




