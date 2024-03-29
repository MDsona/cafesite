from django.db import models

from django.contrib.auth.models import User     #19d
from django.utils import timezone
from django.urls import reverse                 # 22c
from datetime import datetime, date, time       # 27a
# from phonenumber_field.modelfields import PhoneNumberField # 28a

# Create your models here.

class MenuTitle(models.Model):                  # 2a
    title = models.CharField(max_length=100)

    def __str__(self):                          # 2c
        return self.title


class MenuType(models.Model):                   # 6a
    the_type = models.CharField(max_length=100)
    title = models.ForeignKey(MenuTitle, on_delete=models.CASCADE, related_name='title_type_releted')

    def __str__(self):                          # 6c
        return self.the_type


class MenuContent(models.Model):                               # 9a
    content = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # active = models.BooleanField(default=True)
    conOFtype = models.ForeignKey(MenuType, on_delete=models.CASCADE, related_name='con_of_type')

    def __str__(self):
        return ' {} --> {} '.format(self.content, self.conOFtype)


class MapBox(models.Model):                                 # 12a
    mapURL = models.URLField(max_length=500)                # 12a
    mapIMG = models.ImageField(default='default.jpg', upload_to='map_imgs')  # 13a
    mapActive = models.BooleanField(default=False)          # 13d

    def __str__(self):                                      # 12a
        return self.mapURL


class SessionType(models.Model):                            # 18a
    session_type1 = models.CharField(max_length=30, blank=True, verbose_name='نوع الجلسة')
    def __str__(self):
        return self.session_type1

class NumberOFseats(models.Model):                          # 18b
    number_of_seats1 = models.CharField(max_length=10, blank=True, verbose_name='عدد المقاعد', help_text='مثل: 10 مقاعد')
    def __str__(self):
        return self.number_of_seats1


class ForReser(models.Model):                               # 19a>>
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name='الاسم')  # d19d
    session_type = models.ForeignKey(SessionType, on_delete=models.CASCADE, null=False, blank=False, verbose_name='نوع الجلسة')  # a19a
    number_of_seats = models.ForeignKey(NumberOFseats, on_delete=models.CASCADE, null=False, verbose_name='عدد المقاعد')
    #session_duration = models.PositiveSmallIntegerField(help_text='ساعة', null=False, verbose_name='مدة الجلسة')      # c19c
    session_duration = models.CharField(max_length=1, default='1', help_text='ساعة\ساعات', null=False, verbose_name='مدة الجلسة')      # c19c
    # 27a session_date = models.DateTimeField(null=True, help_text='صيغة التوقيت YYYY-MM-DD hh:mm:ss', verbose_name='التوقيت')
    session_date = models.DateField(auto_now=False, null=False, verbose_name='التاريخ')      # 27a
    session_time = models.TimeField(auto_now=False, null=False, verbose_name='التوقيت', help_text='مثال 18:05')      # 27d
    # mobile_number = PhoneNumberField(max_length=14, help_text='مثال:0511111111', null=False, verbose_name='رقم الجوال')  # 28a
    mobile_number = models.CharField(max_length=10, default='05', help_text='مثال:0511111111', null=False, verbose_name='رقم الجوال')
    timestamp = models.DateTimeField(auto_now=True)             # 19d

    def __str__(self):                                          # 19e
        return 'حجز {} في تاريخ {}'.format(self.author, self.session_date)
    
    def get_absolute_url(self):                                 # 22c
        return reverse('reser_detail_url', args=[self.pk])


# blank=True | not required



