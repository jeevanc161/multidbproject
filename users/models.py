from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your models here.

class DatabaseList(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Database List'

class Userdb(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigndb = models.ManyToManyField(DatabaseList , 'assigndb')

    def get_assign_db(self):
        return "\n".join([str(db) for db in self.assigndb.all()])

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'User Databases'
