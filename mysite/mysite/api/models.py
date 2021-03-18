from django.db import models


class My6StockTable(models.Model):
    id = models.IntegerField(primary_key=True)
    stock_code = models.TextField(blank=True, null=True)
    stock_name = models.TextField(blank=True, null=True)
    current_price = models.TextField(blank=True, null=True)
    fluctuation_rate = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    foreigner_investor = models.TextField(blank=True, null=True)
    trading_volume = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my6_stock_table'


class MyStockTable(models.Model):
    id = models.IntegerField(primary_key=True)
    stock_code = models.TextField(blank=True, null=True)
    stock_name = models.TextField(blank=True, null=True)
    current_price = models.TextField(blank=True, null=True)
    fluctuation_rate = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    foreigner_investor = models.TextField(blank=True, null=True)
    trading_volume = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_stock_table'


class StockTable(models.Model):
    stock_code = models.CharField(max_length=20, blank=True, null=True)
    stock_name = models.CharField(max_length=20, blank=True, null=True)
    current_price = models.CharField(max_length=20, blank=True, null=True)
    fluctuation_rate = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.CharField(max_length=20, blank=True, null=True)
    foreigner_investor = models.CharField(max_length=20, blank=True, null=True)
    trading_volume = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_table'


class Users(models.Model):
    user_id = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    name = models.CharField(db_column='NAME', max_length=20)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'