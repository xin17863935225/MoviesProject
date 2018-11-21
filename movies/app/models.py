from django.db import models

# Create your models here.

# 注册登录页面背景图片
class LoginImg(models.Model):
    imgname = models.CharField(max_length=200)
    class Meta:
        db_table = 'mv_loginimg'

# 电影
class Movies(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    downloadlink = models.CharField(max_length=500)
    url = models.CharField(max_length=100)
    class Meta:
        db_table = 'mv_movies'

# 用户
class User(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=128,null=False)
    email = models.CharField(max_length=64, unique=True,null=True)
    sex = models.BooleanField(default=True)
    age = models.IntegerField(max_length=3,default=18)
    icon = models.ImageField(upload_to='upload/',default='default.jpg')
    class Meta:
        db_table = 'mv_user'

# 电影票购物车
class ShoppingCart(models.Model):
    userid = models.ForeignKey(User)
    movieid = models.ForeignKey(Movies)
    price = models.FloatField(max_length=10,default=26)
    # 数量
    quantity = models.IntegerField(max_length=5,default=1)
    # 付款情况
    paystatus = models.BooleanField(default=True)
    # 座位
    seats = models.CharField(max_length=50)

    class Meta:
        db_table = 'mv_shopping'

