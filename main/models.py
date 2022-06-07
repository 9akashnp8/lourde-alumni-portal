from django.db import models

# Create your models here.
class Alumni(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    batch = models.CharField(max_length=100)
    application_no = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Alumni, self).save(*args, **kwargs)
        if not self.application_no:
            prefix = 'LMS-APPL-'
            id = self.id
            self.application_no = prefix+str(id)
            super(Alumni, self).save(*args, **kwargs)
        