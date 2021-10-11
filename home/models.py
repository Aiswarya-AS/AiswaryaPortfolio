from django.db import models

# Create your models here.
class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    value = models.IntegerField()

class Education(models.Model):
    course_name=models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    college_name = models.CharField(max_length=300)
    description = models.TextField()

class Experience(models.Model):
    role = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    company_name = models.CharField(max_length=200,null=True,blank=True)
    point_1  = models.CharField(max_length=500)
    point_2= models.CharField(max_length=500)
    point_3= models.CharField(max_length=500)

class PortfolioDetail(models.Model):
    project_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    project_url  = models.URLField(max_length=200)
    description = models.TextField()
    image_1 = models.ImageField(upload_to ='image/%y/%m/%d')
    image_2 = models.ImageField(upload_to = 'image/%y/%m/%d')
    image_3 = models.ImageField(upload_to ='image/%y/%m/%d')
    

    def __str__(self):
        return self.project_name