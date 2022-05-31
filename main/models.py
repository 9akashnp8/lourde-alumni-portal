from django.db import models

# Create your models here.
class Alumni(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    batch = models.CharField(max_length=100)
    alumni_no = models.CharField(max_length=100)

    def __str__(self):
        return self.name