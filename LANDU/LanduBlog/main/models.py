from django.db import models

class Task(models.Model):
	task_title = models.CharField('task_title' , max_length=70)
	task_text  = models.TextField('task_text' )
	task_image = models.ImageField()

class Hotel(models.Model):
	name = models.CharField(max_length=50)
	hotel_Main_Img = models.ImageField(upload_to='images/')


def __str__(self):
	return self.task_title
   
