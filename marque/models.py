from django.db import models

# Create your models here.
class Mark(models.Model):
    idMark=models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=True)
    descrition = models.CharField(max_length=200, null=True)
    picture=models.CharField(max_length=250,null=True)
    createat=models.DateTimeField(auto_now_add=True, null=True)
    updateAt=models.DateTimeField(auto_now=True, null=True)
    is_active=models.BooleanField(default=True, null=True)
    is_deleted=models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title 


