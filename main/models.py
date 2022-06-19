from django.db import models

# Create your models here.
class Alumni(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    batch = models.CharField(max_length=100)
    application_no = models.CharField(max_length=100, blank=True)
    razor_payment_id = models.CharField(max_length=100, blank=True)
    razor_order_id = models.CharField(max_length=100, blank=True)
    is_paid = models.BooleanField(blank=True)
    alumni_no = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Alumni, self).save(*args, **kwargs)
        if not self.application_no:
            prefix = 'LMS-APPL-'
            id = self.id
            self.application_no = prefix+str(id)
            super(Alumni, self).save(*args, **kwargs)
        if self.razor_payment_id:
            self.is_paid = True
            prefix = 'LMS-ALUM-'
            id = self.id
            self.alumni_no = prefix+str(id)
            super(Alumni, self).save(*args, **kwargs)
        