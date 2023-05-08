from django.contrib import admin
from .models import Course
from .models import User
from .models import UserLocation
from .models import Department

admin.site.register(Course)
admin.site.register(User)
admin.site.register(UserLocation)
admin.site.register(Department)

