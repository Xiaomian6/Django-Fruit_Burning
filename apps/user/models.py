from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    用户
    """
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30, null=True,unique=True,  blank=True, verbose_name="用户名")
    user_gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female", verbose_name="性别")
    user_phone = models.CharField(null=True, blank=True, unique=True,max_length=11, verbose_name="手机号码")
    user_avator = models.ImageField(upload_to="avator/", default="avator/default.jpg",null=True, blank=True, verbose_name="头像")
    user_email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="用户邮箱")
    user_ifrealname = models.BooleanField(default=False, verbose_name="是否实名")
    user_creditscore = models.IntegerField(default=0, verbose_name="信用积分")
    user_importance = models.IntegerField(default=0, verbose_name="会员的重要程度/经验值")
    user_introduction = models.TextField(verbose_name="个人介绍")
    user_exrea = models.TextField(verbose_name="备注")
    roles = models.ManyToManyField("role", verbose_name="角色", blank=True)

    class Meta:
        db_table = 'fb_user'
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.user_name:
            # 如果不为空则返回用户名
            return self.user_name
        else:
            # 如果用户名为空则返回不能为空的对象
            return self.username
        #return self.user_name #如果为name的话，应为name设置为可空的,所以在str转换的时候会出错

class verified(models.Model):
    verified_id = models.AutoField(primary_key=True)
    verified_name = models.CharField(max_length=10,verbose_name="真实姓名")
    verified_idcard = models.CharField(max_length=18,verbose_name="身份证号")
    verified_user = models.ForeignKey(User,related_name="user_verified",null=True, blank=True,verbose_name="实名用户")

    class Meta:
        db_table = 'fb_verified'
        verbose_name = "实名认证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.verified_name

class role(models.Model):
    """
    角色：用于权限绑定
    """
    UNIT_CHOICES = (
        ('1', '普通用户'),
        ('2', '采购'),
        ('3', '收购'),
        ('4', '运输'),
        ('5', '店铺'),
    )
    role_name = models.CharField(max_length=10,default='1',choices=UNIT_CHOICES,unique=True, verbose_name="角色")
    role_permissions = models.CharField(max_length=255, blank=True, verbose_name="角色权限字符串")
    role_extra = models.CharField(max_length=50, blank=True, null=True, verbose_name="备注")
    update_time = models.DateTimeField(auto_now = True,verbose_name="上次更新时间")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        db_table = 'fb_role'
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.role_name

class address(models.Model):
    address_name = models.CharField(max_length=10,verbose_name="姓名")
    address_phone = models.CharField(max_length=11,verbose_name="电话")
    address_address = models.CharField(max_length=50, verbose_name="地址")
    address_user = models.ForeignKey(User,related_name="user_address",null=True, blank=True,verbose_name="所属用户")


    class Meta:
        db_table = 'fb_address'
        verbose_name = "地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address_name