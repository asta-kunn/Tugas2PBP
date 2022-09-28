from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BarangTodolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.TextField()
    description = models.TextField()
    status = models.BooleanField(default=False)


