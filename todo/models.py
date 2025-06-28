from django.db import models
from django.contrib.auth.models import User

class TODO1(models.Model):
    srno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
