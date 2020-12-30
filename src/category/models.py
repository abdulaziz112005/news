from django.db import models
from django.template.defaultfilters import slugify


class Catalog(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)

    class Meta:
        verbose_name = "Catalog"
        verbose_name_plural = "Cataloglar"

class News(models.Model):
    name = models.ForeignKey(Catalog ,on_delete=models.CASCADE)
    photo = models.ImageField(max_length=200,blank=True, upload_to='news')
    info = models.TextField()
    created_date = models.DateTimeField(auto_now=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
class Contact(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contactlar"
