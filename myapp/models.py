from django.db import models


class Super_AdminAccount(models.Model):

    SId = models.AutoField(primary_key=True)
    Fname=models.CharField(max_length=255, default="First Name")
    Lname=models.CharField(max_length=255, default="Last Name")
    Email=models.EmailField(max_length=255, default="Email Name")
    Username=models.CharField(max_length=255, default="Username ")
    Password=models.TextField(max_length=3000, default="Password ")
    ContactNo=models.CharField(max_length=100, default="Contact no")
    def __str__(self):
        return self.Fname

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.CharField(max_length=50,default="")
    review = models.PositiveIntegerField()
    Super_Admin_Id=models.ForeignKey(Super_AdminAccount , on_delete=models.SET_NULL,blank=True,null=True)
    
    def __str__(self):
        return self.title 