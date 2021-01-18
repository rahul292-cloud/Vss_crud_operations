from django.db import models
import datetime

# Create your models here.

class StudentDetails(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    age = models.IntegerField(default=0)
    roll_no = models.IntegerField(default=0)
    class_name = models.CharField(null=False, blank=False, max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            self.created_at = datetime.datetime.now()
            studentDetails_save = super(StudentDetails, self).save(force_insert=False, force_update=False, using=None,
                                                     update_fields=None)
        else:
            self.updated_at = datetime.datetime.now()
            studentDetails_save = super(StudentDetails, self).save(force_insert=False, force_update=False, using=None,
                                                     update_fields=None)
        return studentDetails_save

