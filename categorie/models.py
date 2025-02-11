from django.db import models

# Create your models here.
class Category(models.Model):
    idCategory=models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=True)
    descrition = models.CharField(max_length=200, null=True)
    createat=models.DateTimeField(auto_now_add=True, null=True)
    updateAt=models.DateTimeField(auto_now=True, null=True)
    is_active=models.BooleanField(default=True, null=True)
    is_deleted=models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title