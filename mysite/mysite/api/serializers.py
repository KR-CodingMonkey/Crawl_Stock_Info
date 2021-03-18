from mysite.api.models import My6StockTable, StockTable
from rest_framework import serializers

class My6StockTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = My6StockTable
        fields = ['id', 'stock_code', 'stock_name', 'current_price', 'fluctuation_rate', 'created_at', 'foreigner_investor', 'trading_volume']

        read_only_fileds = ('stock_code', 'stock_name', 'current_price',)


class StockTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTable
        fields = ['stock_code', 'stock_name', 'current_price', 'fluctuation_rate', 'created_at', 'foreigner_investor', 'trading_volume']

        # read_only_fileds = ('stock_code', 'stock_name', 'current_price',)