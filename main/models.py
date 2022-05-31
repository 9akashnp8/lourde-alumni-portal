from django.db import models

# Create your models here.
class Alumni(models.Model):
    alumni_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    batch = models.CharField(max_length=100)
    alumni_no = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Alumni, self).save(*args, **kwargs)
        if not self.alumni_no:
            prefix = 'LMS-ALUM-'
            id = self.alumni_id
            self.alumni_no = prefix+str(id)
            super(Alumni, self).save(*args, **kwargs)
        