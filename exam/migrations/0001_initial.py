# Generated by Django 3.1.3 on 2020-11-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_Name', models.CharField(max_length=100)),
                ('Client_Name', models.CharField(max_length=100)),
                ('Exam_Start_Date', models.DateField()),
                ('Exam_End_Date', models.DateField()),
                ('Number_of_Regions', models.IntegerField()),
                ('Number_of_Exam_Centers', models.IntegerField()),
            ],
        ),
    ]
