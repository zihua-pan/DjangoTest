from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='问题描述')
    pub_date = models.DateTimeField(verbose_name='发布日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_fields = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布'

    class Meta:
        verbose_name = "问题"
        verbose_name_plural = "我的问题"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #定义级联删除
    choice_text = models.CharField(max_length=200, verbose_name='选项信息')
    votes = models.IntegerField(default=0, verbose_name='投票数量')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "选项"
        verbose_name_plural = "我的选项"
