"""studyspaceservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api.views import StudyHallView, EhallView, EhallDetailView, EhallDetailsView, StudentView, StudentDetailsView, \
CourseView, CourseDetailsView, EnquiryView, EnquiryDetailsView, ExpenseView, ExpenseDetailsView, ExpenseSerializerView
from rest_framework.views import APIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^studyhall/$', StudyHallView.as_view()),
    url(r'^studyhall/([0-9]+)/$', EhallDetailView.as_view()),
    url(r'^e_hall/$', EhallView.as_view()),
    url(r'^e_hall/([0-9]+)/$', EhallDetailsView.as_view()),
    url(r'^e_student/$', StudentView.as_view()),
    url(r'^e_student/([0-9]+)/$', StudentDetailsView.as_view()),
    url(r'^e_course/$', CourseView.as_view()),
    url(r'^e_course/([0-9]+)/$', CourseDetailsView.as_view()),
    url(r'^e_enquiry/$', EnquiryView.as_view()),
    url(r'^e_enquiry/([0-9]+)/$', EnquiryDetailsView.as_view()),
    url(r'^e_expense/$', ExpenseView.as_view()),
    url(r'^e_expense/([0-9]+)/$', ExpenseDetailsView.as_view()),
    url(r'^e_expense_serializer/$', ExpenseSerializerView.as_view()),
]
