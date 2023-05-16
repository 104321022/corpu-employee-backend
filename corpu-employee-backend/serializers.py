from rest_framework import serializers
from .models import Course
from .models import User
from .models import UserLocation
from .models import Department
from .models import Assessment
from .models import Timetable

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

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ["staff_id", "employee_id", "course_code"]

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ["user_id", "course_code", "monday_time", "tuesday_time", "wednesday_time", "thursday_time", "friday_time"]

