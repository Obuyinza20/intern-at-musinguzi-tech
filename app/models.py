from django.db import models

# Create your models here.



class Photo(models.Model):
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.description
    
class Internee(models.Model):
    first_name = models.CharField(max_length=200 ,null=False, blank = False)
    second_name = models.CharField(max_length=200, null=False, blank = False)
    institution = models.CharField(max_length=500 ,null=False, blank = False)
    course = models.CharField(max_length=500 ,null=False, blank = False)
    gender = models.CharField(max_length=100 ,null=False, blank = False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=200 ,null=False, blank = False)
    period = models.CharField(max_length=100)
    willingness = models.CharField(max_length=200 ,null=False, blank = False)
    area_of_interest = models.CharField(max_length=500 ,null=False, blank = False)

    def __str__(self) -> str:
        return self.first_name
    
    
