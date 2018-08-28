# encoding: utf-8

from __future__ import unicode_literals

from datetime import datetime
from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.


class Zclist(models.Model):
    bianhao = models.CharField(max_length=50, verbose_name=u"资产编号")
    zcname = models.CharField(max_length=16, verbose_name=u"资产名称")
    guige = models.CharField(max_length=300,default=u'请填写详细型号信息',verbose_name=u"规格型号")
    zcconditons = models.CharField(max_length=8,verbose_name=u"资产状态",default=u"正常")
    cgdate = models.DateTimeField(default=datetime.now, verbose_name=u"购置日期")
    guanlibm = models.CharField(max_length=12,verbose_name=u"管理部门",default=u"行政管理中心")
    guanliadmin = models.CharField(max_length=10,verbose_name=u"管理员工",default=u"李秀娜")
    cfangwz = models.CharField(max_length=10,verbose_name=u"存放位置",default=u"E谷办公区")
    shiyongzk = models.CharField(max_length=10,verbose_name=u"使用状况")
    zcdanwei = models.CharField(max_length=10,verbose_name=u"资产单位",default=u"台")
    zcjz = models.FloatField(default=0,max_length=12,verbose_name=u"资产净值")
    shiyongbm = models.CharField(max_length=16,verbose_name=u"领用部门")
    shiyongyg = models.CharField(max_length=12,verbose_name=u"领用员工")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")


    class Meta:
        verbose_name = u"资产列表"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.bianhao
