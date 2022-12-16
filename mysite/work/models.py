from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class work_plan(models.Model):
    data_w = models.DateField(max_length=10)
    time_w = models.TimeField(max_length=10)
    work_w = models.CharField(max_length=30, blank=False)
    fio_w = models.CharField(max_length=20, blank=False)
    tel_w = models.CharField(max_length=20, blank=False)
    comlete_w = models.BooleanField(default=False)
    created_w = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f' Услуга - {self.work_w} Подтверждение -  {self.comlete_w}'