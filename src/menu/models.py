from django.db import models

from django.contrib.auth.models import User     #19d
from django.utils import timezone
from django.urls import reverse                 # 22c

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='الاسم')  # d19d
    session_type = models.ForeignKey(SessionType, on_delete=models.CASCADE, blank=True, null=True, verbose_name='نوع الجلسة')  # a19a
    number_of_seats = models.ForeignKey(NumberOFseats, on_delete=models.CASCADE, blank=True, null=True, verbose_name='عدد المقاعد')
    session_duration = models.FloatField(help_text='ساعة', blank=True, null=True, verbose_name='مدة الجلسة')      # c19c
    session_date = models.DateTimeField(null=True, blank=True, help_text='YY-MM-DD hh:mm:ss', verbose_name='التوقيت')
    mobile_number = models.CharField(max_length=10, help_text='مثال:0511111111', blank=True, null=True, verbose_name='رقم الجوال')
    timestamp = models.DateTimeField(auto_now=True)             # 19d

    def __str__(self):                                          # 19e
        return 'حجز {} في تاريخ {}'.format(self.author, self.session_date)
    
    def get_absolute_url(self):                                 # 22c
        return reverse('reser_detail_url', args=[self.pk])





