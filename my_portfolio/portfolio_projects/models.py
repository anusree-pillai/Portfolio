from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    
    def __str__(self) :
        return self.title

class Skill(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Education(models.Model):
    degree = models.CharField(max_length=100) 
    institution = models.CharField(max_length=500)
    graduation_year = models.DateField()

    def __str__(self):
        return f"{self.degree} from {self.institution} ({self.graduation_year})"  
    
class Workexperience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __self__(self):
        return f"{self.job_title} at {self.company}"
    
class about(models.Model):
    description = models.CharField(max_length=500)
    resume_url = models.URLField()
    image = models.ImageField()

    def __self__(self):
        return self.description,self.resume_url,self.image
        


    






