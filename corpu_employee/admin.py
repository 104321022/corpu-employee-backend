from django.contrib import admin
from .models import Course
from .models import User

admin.site.register(Course)
admin.site.register(User)
