from .models import Course
from .models import User
from .models import UserLocation
from .models import Department
from .models import Assessment
from .models import Timetable

from .serializers import CourseSerializer
from .serializers import UserSerializer
from .serializers import UserLocationSerializer
from .serializers import DepartmentSerializer
from .serializers import AssessmentSerializer
from .serializers import TimetableSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def course_list(request, format=None):

    # Get all the courses
    courses = Course.objects.all()
    # Serialize
    serializer = CourseSerializer(courses, many=True)
    # return Json
    return Response({"courses": serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_course(request, format=None):

    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def course(request, course_code, format=None):

    try:
        course = Course.objects.get(pk=course_code)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def signin(request, format=None):

    request_data = request.data
    try:
        user = User.objects.get(
            email=request_data['email'],
            password=request_data['password']
        )
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def signup(request, format=None):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_user_location(request, format=None):
    try:
        user_location = UserLocation.objects.get(
            user_id=request.data["user_id"]
        )
    except UserLocation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserLocationSerializer(user_location)
    return Response(serializer.data, status=status.HTTP_200_OK)
      
@api_view(["POST"])
def update_user_location(request, format=None):
    serializer = UserLocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def add_department(request, format=None):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def get_departments(request, format=None):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response({"departments": serializer.data}, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_assessment(request, format=None):
    serializer = AssessmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def get_assessments(request, format=None):

    request_data = request.data
    try:
        user_id = request_data['user_id']
        assessments = Assessment.objects.get(
            user_id=user_id
        ).all()
    except Assessment.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
 
    serializer = AssessmentSerializer(assessments, many=True)
    return Response({"assessments": serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def assessment_details(request, format=None):
    request_data = request.data
    try:
        assessment = Assessment.objects.get(
            assessment_id=request_data["id"]
        )
    except Assessment.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AssessmentSerializer(assessment)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_timetable(request, format=None):
    serializer = TimetableSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_timetable(request, format=None):
    request_data = request.data

    try:
        time_table = Timetable.objects.get(
            course_code=request_data["course_code"]
        )
    except Timetable.DoesNotExist:        
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TimetableSerializer(time_table)
    return Response(serializer.data, status=status.HTTP_200_OK)


