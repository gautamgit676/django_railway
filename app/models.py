from django.db import models

# Create your models here.
class SCHOOL(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    established_year = models.PositiveBigIntegerField()
    photo = models.ImageField(upload_to='school_photos/',null=True,
    blank=True)
    def __str__(self):
        return self.name
