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
    details = models.JSONField(null=True)


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


class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True, unique=True)
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applicant')
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    details = models.JSONField(null=True)

    def __str__(self):
        return 'Assessment for ' + self.course_code.course_title + ' - ' + ', Creator: ' + self.staff_id.first_name + ' ' + self.staff_id.last_name + ' - ' +  ', Applicant: ' + self.employee_id.first_name + ' ' + self.employee_id.last_name

class Timetable(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    monday_time = models.JSONField(null=True)
    tuesday_time = models.JSONField(null=True)
    wednesday_time = models.JSONField(null=True)
    thursday_time = models.JSONField(null=True)
    friday_time = models.JSONField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'course_code'], name='user_course_timetable'
            )
        ]

    def __str__(self):
        if self.user_id == None:
            return 'Timetable for: ' + self.user_id.first_name + ' ' + self.user_id.last_name
        elif self.course_code == None:
            return 'Timetable for: ' +  self.course_code.course_title
        else:
            return 'Timetable of: ' + self.course_code.course_title + ', Created by: ' + self.user_id.first_name + ' ' + self.user_id.last_name

class JobApplication(models.Model):
    applicant_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.CharField(max_length=29)
    status = models.CharField(max_length=9, null=True)
    data = models.JSONField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['applicant_id', 'course_code'], name='user_course_application'
            )
        ]

    def __str__(self):
        return 'Job Application of ' + self.applicant_id.first_name + ' ' + self.applicant_id.last_name + ' for course ' + self.course_code.course_title
