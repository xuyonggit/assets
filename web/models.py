from django.db import models


# Create your models here.
class Asset(models.Model):
    id = models.AutoField(primary_key=True) # 序号
    assets_id = models.CharField(max_length=255, default=None)  # 资产编号
    assets_name = models.CharField(max_length=255, default=None)    # 资产名称
    assets_brand = models.CharField(max_length=255, default=None)   # 品牌
    assets_version = models.CharField(max_length=255, default=None) # 型号
    buying_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)      # 购买价格
    buying_date = models.DateField(default=None)        # 购买日期
    notes = models.CharField(max_length=1024, default=None)     # 备注

    def __unicode__(self):
        return self.assets_id, self.assets_brand, self.assets_version