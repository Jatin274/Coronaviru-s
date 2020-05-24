from django.db import models

class Coronafighters(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    des = models.CharField(max_length=2000, null=True, blank=True)
    img1 = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.Name

class News(models.Model):
    img1= models.FileField(null=True,blank=True)
    source=models.CharField(max_length=50,null=True,blank=True)
    time= models.CharField(max_length=50,null=True,blank=True)
    heading= models.CharField(max_length=50,null=True,blank=True)
    des =models.CharField(max_length=2000,null=True,blank=True)
    link=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.heading

