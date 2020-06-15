from django.db import models

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

    def __str__(self):                                      # 12a
        return self.mapURL



