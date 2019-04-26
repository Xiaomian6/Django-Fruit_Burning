from django.db import models

# Create your models here.
from user.models import *
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone
class task(models.Model):
    STATUS_CHOICES = (
        ('0', '任务已取消'),
        ('1', '任务等待接受'),
        ('2', '任务已接受'),
        ('3', '已完成任务'),
        ('4', '任务超出截止日期'),
        ('5', '待审核任务'),

    )
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=30,verbose_name="任务标题")
    task_desc = UEditorField(verbose_name="任务描述", imagePath="task/images/", width=1000, height=300,
                              filePath="task/files/", default='')
    task_price = models.FloatField(default=0.0,verbose_name="任务价格")
    task_status = models.CharField(max_length=10,choices=STATUS_CHOICES,verbose_name="任务状态")

    task_type = models.BooleanField(default=False,verbose_name="接受任务或者发布任务")
    task_deposit = models.IntegerField(verbose_name="任务押金金额")
    task_deposit_status = models.IntegerField(verbose_name="任务押金状态")
    task_updateTime = models.DateTimeField(auto_now=True,verbose_name="任务最近更新时间")
    task_releaseTime = models.DateTimeField(auto_now_add=True,verbose_name="任务发布时间")
    task_receiveTime = models.DateTimeField(default = timezone.now,verbose_name="任务领取时间")
    task_deadline = models.DateTimeField(default = timezone.now, verbose_name="任务截止时间")
    task_extra = models.TextField(verbose_name="任务备注")
    role = models.ManyToManyField(role, verbose_name="任务角色", blank=True)


    class Meta:
        db_table = 'fb_task'
        verbose_name = "任务"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task_title

class task_media(models.Model):
    task_mediaId = models.AutoField(primary_key=True)
    task_mediaurl = models.ImageField(upload_to="task_media/", default="task_media/default.jpg",null=True, blank=True, verbose_name="任务媒体资源")
    task_index = models.IntegerField(verbose_name="任务媒体索引")
    task_id = models.ForeignKey(task,related_name="task_media",null=True, blank=True, verbose_name="所属任务id")

    class Meta:
        db_table = 'fb_task_media'
        verbose_name = "任务媒体"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.task_id)