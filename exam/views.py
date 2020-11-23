from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from django.views.generic import CreateView
from .models import Details


# Create your views here.

class HomePageView(TemplateView):
    template_name = "base.html"

class ExamCreateView(CreateView):
    model = Details
    template_name = "exam_details.html"
    fields = ('Exam_Name','Client_Name','Mock_Start_Date','Mock_End_Date','Exam_Start_Date','Exam_End_Date','Number_of_Regions','Number_of_Exam_Centers')
