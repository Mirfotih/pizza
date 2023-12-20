from django.db import models

# Create your models here.
class MainScrollModel(models.Model):
    image = models.ImageField(upload_to='main-scroll')
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=255)
    discount = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name =  'scroll'
        verbose_name_plural =  'scroll'

class Our_Menus(models.Model):
    image_menus = models.ImageField(upload_to='main-menus')
    title_menus = models.CharField(max_length=50)
    info_menus = models.CharField(max_length=255)
    money = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title_menus

    class Meta:
        verbose_name =  'menus'
        verbose_name_plural =  'menus'




