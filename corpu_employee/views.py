from .models import Course
from .models import User
from .models import UserLocation
from .models import Department
from .models import Assessment
from .models import Timetable
from .models import JobApplication

from .serializers import CourseSerializer
from .serializers import UserSerializer
from .serializers import UserLocationSerializer
from .serializers import DepartmentSerializer
from .serializers import AssessmentSerializer
from .serializers import TimetableSerializer
from .serializers import JobApplicationSerializer

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
    user_data = serializer.data
    del user_data['password']
    return Response(user_data, status=status.HTTP_200_OK)

@api_view(["POST"])
def signup(request, format=None):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user_data = serializer.data
        del user_data['password']
        return Response(user_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
def update_profile(request, format=None):
    try:
        user = User.objects.filter(
            user_id=request.data['user_id']
        )
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.update(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        contact_no=request.data['contact_no'],
        details=request.data['details'],
    )
    return Response(request.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_users_for_assessment(request, format=None):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    users_list = []
    for user in serializer.data:
        if user.user_type == "Employee":
            users_list.append(user)
    return Response({"3": users_list}, status=status.HTTP_200_OK)

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
    assessments = Assessment.objects.all()
    serializer = AssessmentSerializer(assessments, many=True)
    assessments_list = []
    try:
        if request_data['user_type'] == 'staff':
            for item in serializer.data:
                if item['staff_id'] == request_data['user_id']:
                    assessments_list.append(item)
        else:
            for item in serializer.data:
                if item['employee_id'] == request_data['user_id']:
                    assessments_list.append(item)
    except Assessment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    for assessment in assessments_list:
        staff_user=User.objects.get(
            user_id=assessment['staff_id']
        )
        assessment['staff_name'] = staff_user.first_name + ' ' + staff_user.last_name
        employee_user=User.objects.get(
            user_id=assessment['employee_id']
        )
        assessment['employee_name'] = employee_user.first_name + ' ' + employee_user.last_name
    
    return Response({"assessments": assessments_list}, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_employees_for_staff(request, format=None):
    request_data = request.data
    staff_id = request_data['staff_id']

    employees = []
    assessments_serializer = AssessmentSerializer(Assessment.objects.all(), many=True)
    assessments = []
    for assessment in assessments_serializer.data:
        if assessment['staff_id'] == staff_id:
            assessments.append(assessment)

    for assessment in assessments:
        data = {}
        user = User.objects.get(
            user_id=assessments['employee_id']
        )
        course = Course.objects.get(
            course_code=assessments['course_code']
        )
        data['employee_id'] = user.user_id
        data['employee_name'] = user.first_name + ' ' + user.last_name
        data['course_code'] = assessments['course_code']
        data['course_title'] = course.course_title

        employees.append(data)

    return Response({"employees": employees}, status=status.HTTP_200_OK)
    

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

@api_view(["GET"])
def get_applications_for_course(request, format=None):
    request_data = request.data

    job_applications_serializer = JobApplicationSerializer(JobApplication.objects.all(), many=True)
    job_applications_list = []

    for job_application in job_applications_serializer.data:
        if job_application['course_code'] == request_data['course_code']:
            user = User.objects.get(
                user_id=job_application['applicant_id']
            )
            job_application_map = {}
            job_application_map = job_application
            job_application_map['first_name'] =user.first_name
            job_application_map['last_name'] =user.last_name
            job_applications_list.append(job_application)

    return Response({"applications": job_applications_list}, status=status.HTTP_200_OK)

@api_view(["POST"])
def post_job_application(request, format=None):
    serializer = JobApplicationSerializer(data=request.data)
    if serializer.is_valid():
        try:
            job_application_response = {}
            job_application = JobApplication.objects.get(
                applicant_id=request.data['applicant_id'],
                course_code=request.data['course_code']
            )
            job_application_response['data'] = JobApplicationSerializer(job_application).data
            job_application_response['message'] = 'Application already exists'
            return Response(job_application_response, status=status.HTTP_400_BAD_REQUEST)
        except JobApplication.DoesNotExist:            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

