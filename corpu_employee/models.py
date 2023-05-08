from django.db import models
from django.conf import settings

class Course(models.Model):
    course_code = models.CharField(primary_key=True, max_length=9, unique=True)
    course_title = models.CharField(max_length=99, unique=True)
    pre_requisite = models.ForeignKey(
        "self", blank=True, default="", on_delete=models.CASCADE, null=True
    )
    description = models.CharField(max_length=499, blank=True, default="")

    def __str__(self):
        return self.course_title + " (" + self.course_code + " )"

class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=14)
    email = models.CharField(max_length=29, unique=True)
    contact_no = models.CharField(max_length=14, unique=True)
    user_type = models.CharField(max_length=9)
    password = models.CharField(max_length=19)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class UserLocation(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    latutude = models.CharField(max_length=19)
    longiture = models.CharField(max_length=19)
    address = models.CharField(max_length=99)

    def __str__(self):
        return self.address

class Department(models.Model):
    departmant_id = models.CharField(primary_key=True, max_length=9, unique=True)
    name = models.CharField(max_length=19)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.manager.first_name + ' ' + self.manager.last_name


