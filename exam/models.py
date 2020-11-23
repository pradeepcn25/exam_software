from django.db import models

# Create your models here.
class Details(models.Model): 
  
    # fields of the model 
    Exam_Name = models.CharField(max_length = 100) 
    Client_Name = models.CharField(max_length = 100)
    Mock_Start_Date = models.DateField()
    Mock_End_Date = models.DateField()
    Exam_Start_Date = models.DateField()
    Exam_End_Date = models.DateField()
    Number_of_Regions = models.IntegerField()
    Number_of_Exam_Centers = models.IntegerField()
  
    # renames the instances of the model 
    # with their title name 
    def __str__(self): 
        return self.Exam_Name 