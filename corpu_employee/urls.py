"""
URL configuration for corpu_employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from corpu_employee import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("courses/", views.course_list),
    path("add_course/", views.add_course),
    path("course/<str:course_code>", views.course),
    path("signin/", views.signin),
    path("signup/", views.signup),
    path("getUserLocation/", views.get_user_location),
    path("updateUserLocation/", views.update_user_location),
    path("departments/", views.get_departments),
    path("addDepartment/", views.add_department),
    path("createAssessment/", views.create_assessment),
    path("getAssessments/", views.get_assessments),
    path("assessmentDetails/", views.assessment_details),
    path("submitAssessment", views.submit_assessment),
    path("approveAssessment", views.approve_assessment),
    path("createTimetable/", views.create_timetable),
    path("getTimetable/", views.get_timetable),
    path("getUsersForAssessment", views.get_users_for_assessment),
    path("getApplicationsForCourse", views.get_applications_for_course),
    path("postJobApplication", views.post_job_application),
    path("updateProfile", views.update_profile),
]

urlpatterns = format_suffix_patterns(urlpatterns)