from django.db import models

# Create your models here.
class extract_image(models.Model):

   due_date = models.CharField(max_length=50)
   account_no = models.CharField(max_length=50)
   bill_amount = models.CharField(max_length=50)


   def __unicode__(self):
      return self.name
