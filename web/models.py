from django.db import models


# Create your models here.
class Asset(models.Model):
    id = models.AutoField(primary_key=True) # 序号
    assets_id = models.CharField(max_length=255, default=None)  # 资产编号
    assets_name = models.CharField(max_length=255, default=None)    # 资产名称
    assets_brand = models.CharField(max_length=255, default=None)   # 品牌
    assets_version = models.CharField(max_length=255, default=None)     # 型号
    buying_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)      # 购买价格
    buying_date = models.DateField(default='1997-01-01')        # 购买日期
    notes = models.CharField(max_length=1024, default=None)     # 备注
    asset_status = models.IntegerField(default=0)  # 资产状态：0:未知 1:使用中 2:闲置中

    def __unicode__(self):
        return self.assets_id, self.assets_brand, self.assets_version


class Asset_detial(models.Model):
    id = models.AutoField(primary_key=True)  # 序号
    assets_id = models.CharField(max_length=255, default=None)  # 资产编号
    create_date = models.DateField(default=None)    # 创建日期
    create_type = models.CharField(max_length=255, default=None)    # 类型
    use_department = models.CharField(max_length=255, default=None)     # 使用部门
    use_people = models.CharField(max_length=255, default=None)     # 使用人

    def __unicode__(self):
        return self.assets_id


class department(models.Model):
    department_name = models.CharField(u'部门名称', max_length=255, null=False, default=None)

    def __str__(self):
        return self.department_name