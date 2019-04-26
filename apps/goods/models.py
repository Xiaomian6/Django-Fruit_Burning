from django.db import models
from user.models import *
from DjangoUeditor.models import UEditorField

from datetime import datetime

# Create your models here.
class shop(models.Model):
    """
       店铺
       """
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=20,verbose_name="店铺名")
    shop_address = models.CharField(max_length=50,verbose_name="店铺地址")
    shop_phone = models.CharField(max_length=11,verbose_name="联系方式")
    shop_extra = models.TextField(verbose_name="店铺信息")
    shop_updateTime = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    user = models.OneToOneField(User,null=True, blank=True,verbose_name="所属用户")


    class Meta:
        db_table = 'fb_shop'
        verbose_name = "店铺"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.shop_name

class goods(models.Model):
    """
       商品
       """
    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=30,verbose_name="商品名")
    goods_price = models.FloatField(default=0, verbose_name="商品价格")
    goods_pickTime = models.DateTimeField(default=datetime.now, verbose_name="采摘日期")
    goods_shelflife = models.IntegerField(verbose_name="商品保质期")
    goods_desc = UEditorField(verbose_name="商品详情", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    goods_front_image = models.ImageField( verbose_name="外面封面图",upload_to="goods/images/", null=True, blank=True)
    goods_weight = models.CharField(max_length=10, verbose_name="商品重量")
    goods_updateTime = models.DateTimeField(auto_now=True, verbose_name="商品上次更新时间")
    goods_extra = models.TextField( verbose_name="商品备注")
    goods_title = models.CharField(max_length=100, verbose_name="商品标题")
    goods_productarea = models.CharField(max_length=20, verbose_name="产地")
    goods_dateadded = models.DateTimeField(auto_now_add=True, verbose_name="上架日期")
    goods_post = models.BooleanField( verbose_name="是否承担运费")
    goods_stock = models.IntegerField(default=0, verbose_name="总库存")
    shop = models.ForeignKey(shop,null=True, blank=True,verbose_name="所属店铺")


    class Meta:
        db_table = 'fb_goods'
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name


class goodsimage(models.Model):
    """
    商品里面的轮播图
    """
    goods = models.ForeignKey(goods, verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = 'fb_goodsimage'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.goods_name

