from django.db import models


class Course(models.Model):
    course_code = models.CharField(primary_key=True, max_length=9, unique=True)
    course_title = models.CharField(max_length=99, unique=True)
    pre_requisite = models.ForeignKey(
        "self", blank=True, default="", on_delete=models.CASCADE
    )
    description = models.CharField(max_length=499, blank=True, default="")

    def __str__(self):
        return self.course_title + " (" + self.course_code + " )"
