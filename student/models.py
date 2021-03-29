from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    born = models.DateField()
    city_of_registration = models.CharField(max_length=100)
    group = models.CharField(max_length=50)
    course = models.IntegerField()
    is_need_dorm = models.BooleanField()
    dorm_form = models.OneToOneField(to='Dorm_form', on_delete=models.CASCADE, null=True, blank=True)
    dorm_final = models.OneToOneField(to='Dorm_final', on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(to='Rooms', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


    def __str__(self):
        return ' '.join([self.surname, self.name, self.patronymic])


class Rooms(models.Model):
    number = models.CharField(max_length=50)
    places = models.IntegerField()

    def __str__(self):
        return self.number


class Dorm_form(models.Model):
    iq = models.IntegerField()
    kids_in_family = models.IntegerField()
    whats_number = models.IntegerField()
    Friends_count = models.IntegerField()
    q1 = models.BooleanField()
    q2 = models.BooleanField()
    q3 = models.BooleanField()


class Dorm_final(models.Model):
    service_quality = models.IntegerField()
    neighborhood = models.IntegerField()
    q1 = models.BooleanField()
    q2 = models.BooleanField()
    q3 = models.BooleanField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
