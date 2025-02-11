from django.db import models

# Create your models here.
class Maladies(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    pathologie = models.TextField()
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True, null=True)
    is_deleted=models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.titre
