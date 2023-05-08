from rest_framework import serializers
from .models import Course
from .models import User
from .models import UserLocation
from .models import Department

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["course_code", "course_title", "pre_requisite", "description"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "first_name", "last_name", "email", "contact_no", "user_type"]

class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ["user_id", "latitude", "longitude", "address"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["departmant_id", "name", "manager"]


