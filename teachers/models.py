from nturl2path import url2pathname
from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=30)
    course_code=models.CharField(max_length=30)
    departments_choices=(
        ("computer science",'CSE'),
        ("electrical and comunication engineering",'ECE'),
        ("electrical and electronic engineering",'EEE'),
        ("civil engineering",'CIVIL'),
        )
    department = models.CharField(max_length=50,choices=departments_choices,default="CSE")
    url = models.URLField()