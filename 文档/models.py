from django.db import models

# Create your models here.
class album(models.Model):#相册模型
    albumId = models.AutoField
    albumName = models.CharField(max_length=20)#相册名不能大于20个字
    albumUrl = models.TextField
    date = models.DateField
class album_desc(models.Model):
    albumId = models.AutoField
    desc = models.CharField(max_length=255)#描述不能大于255个字
class album_user(models.Model):
    albumId = models.AutoField
    userId = models.AutoField
class imgs(models.Model):
    pic = models.ImageField(upload_to='/demo/static/images')
    imgId = models.AutoField
    imgUrl = models.TextField
    date = models.DateField(auto_now_add=True)
class praise(models.Model):
    albumId = models.AutoField
    num = models.AutoField
class send(models.Model):
    albumId = models.AutoField
    sendNum = models.AutoField
class user(models.Model):
    userId = models.AutoField
    userName = models.CharField(max_length=255)#用户名不能大于255个字
    pswd = models.CharField(max_length=255)#密码不能大于255个字
class user_id(models.Model):
    userId = models.AutoField
    imgId = models.AutoField
