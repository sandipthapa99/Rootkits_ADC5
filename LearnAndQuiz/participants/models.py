from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Profile(models.Model):
	participants = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to="users/profile_pics")

	def __str__(self):
		return f'{self.participants.username} Profile'
		 

class Question(models.Model):
	ques = models.TextField()
	correct_ans = models.CharField(max_length = 20)
	title = models.ForeignKey(Course, on_delete = models.CASCADE)

	def __str__(self):
		return self.ques


class Answer(models.Model):
	ans = models.CharField(max_length=20)
	ques = models.ForeignKey(Question, on_delete = models.CASCADE)

	def __str__(self):
		return self.ans
