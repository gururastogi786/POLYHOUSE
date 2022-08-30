from django.db import models

# Create your models here.

class contactUs(models.Model):


    name = models.CharField(max_length=50)
    number = models.IntegerField()

  #  num = models.IntegerField()
  
  
    def __str__(self):
      return self.name
    
class signup(models.Model):
      
      
      name = models.CharField(max_length=50)
      number = models.IntegerField()
      State = models.CharField(max_length=50)
      district = models.CharField(max_length=50)
      village = models.CharField(max_length=50)
      password = models.CharField(max_length=50)
      c_pass = models.CharField(max_length=50)


      def __str__(self):
        return self.name


 
 



  
  
