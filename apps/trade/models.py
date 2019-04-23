from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from goods.models import goods,shop
from datetime import datetime

class shoppingcart(models.Model):
    """
        购物车
        """
    user = models.ForeignKey(User,null=True, blank=True,verbose_name="所属用户")
    goods = models.ForeignKey(goods,null=True, blank=True,verbose_name="商品")
    shoppingcart_nums = models.IntegerField(default=0, verbose_name="购买数量")
    shoppingcart_addtime = models.DateTimeField(default=datetime.now,verbose_name="商品加入时间")

    class Meta:
        db_table = 'fb_shoppingcart'
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")
    def __str__(self):
        return "%s(%d)".format(self.goods_id.goods_name, self.shoppingcart_nums)


class order(models.Model):
    """
        订单
        """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("paying", "待支付"),
    )
    user = models.ForeignKey(User, null=True, blank=True, verbose_name="用户")
    order_id = models.AutoField(primary_key=True)
    order_nun = models.CharField(max_length=30, verbose_name="订单号")
    order_transationnun = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="交易号")
    order_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="订单状态")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    order_paytime = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
    order_extra = models.TextField(verbose_name="备注")

    order_logistics = models.CharField(max_length=30,verbose_name="物流信息")
    order_updatetime = models.DateTimeField(auto_now=True,verbose_name="订单更新时间")
    order_addtime = models.DateTimeField(auto_now_add=True,verbose_name="下单时间")
    shop = models.ForeignKey(shop, null=True, blank=True, verbose_name="店铺")
    class Meta:
        db_table = 'fb_order'
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_nun)

class order_goods(models.Model):
    """
        订单的商品详情
        """
    order_goods_id = models.AutoField(primary_key=True)
    goods_num = models.IntegerField(default=0,verbose_name="商品数量")
    order_goods_addtime = models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    order = models.ForeignKey(order, verbose_name="订单信息", related_name="goods")
    goods = models.ForeignKey(goods,verbose_name="商品")

    class Meta:
        db_table = 'fb_order_goods'
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_nun)