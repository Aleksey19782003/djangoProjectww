from django.db import models

class ModelAlex(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    prof = models.CharField(max_length=10)


class ModelAlexImg(models.Model):
    name = models.CharField(max_length=10)
    img = models.ImageField(upload_to='img')

class ModelReg(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    user_session = models.CharField(max_length=10)
    user_image = models.CharField(null=True, max_length=100)
    bot_btn = models.CharField(null=True, max_length=10)
    login = models.CharField(max_length=10)


class Img(models.Model):
    Image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=30)
#пример модели


class ProfileImg(models.Model):
    user_image = models.ImageField(upload_to='app/static/img', verbose_name=u'Ваше фото')