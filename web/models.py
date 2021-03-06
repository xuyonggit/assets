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
    asset_status = models.IntegerField(default=0)  # 资产状态：0:未知 1:使用中 2:闲置中 3:故障中

    def __unicode__(self):
        return self.assets_id, self.assets_brand, self.assets_version


class Asset_detial(models.Model):
    id = models.AutoField(primary_key=True)  # 序号
    assets_id = models.CharField(max_length=255, default=None)  # 资产编号
    create_date = models.DateField(default=None)    # 创建日期
    create_type = models.CharField(max_length=255, default=None)    # 类型
    use_department = models.CharField(max_length=255, default=None)     # 使用部门
    use_people = models.CharField(max_length=255, default=None)     # 使用人
    operuser = models.CharField(max_length=255, default=None)       # 操作人

    def __unicode__(self):
        return self.assets_id


class Asset_trouble(models.Model):
    id = models.AutoField(primary_key=True)  # 序号
    assets_id = models.CharField(max_length=255, default=None)  # 资产编号
    trouble_date = models.DateField(default=None)  # 故障日期
    trouble_department = models.CharField(max_length=255, default=None)      # 损坏部门
    trouble_people = models.CharField(max_length=255, default=None)     # 损坏人
    trouble_info = models.CharField(max_length=4096, default=None)      # 故障详情
    operator_user = models.CharField(max_length=255, default=None)      # 操作人

    def __unicode__(self):
        return self.assets_id


class department(models.Model):
    Tixi_name = models.CharField(u'体系名称', max_length=255, null=False, default=None)
    department_name = models.CharField(u'部门名称', max_length=255, null=False, default=None)

    def __str__(self):
        return self.department_name


class baseall(models.Model):
    department_name = models.CharField(u'部门名称', max_length=255, null=False, default=None)    # 部门名称
    pname = models.CharField(u'姓名', max_length=255, null=False, default=None)  # 责任人
    assets_count = models.IntegerField(u'资产数量', default=0)   # 名下资产数量
    trouble_count = models.IntegerField(u'故障资产数量', default=0)   # 名下故障资产数量
