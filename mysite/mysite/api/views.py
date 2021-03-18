from rest_framework import viewsets
from rest_framework import permissions
from mysite.api.models import My6StockTable, StockTable
from mysite.api.serializers import My6StockTableSerializer, StockTableSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

from mysite.recommend_stock import Recommend_Stock

class My6TopicTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = My6StockTable.objects.all()
    serializer_class = My6StockTableSerializer

    permission_classes = [permissions.IsAuthenticated]

    # /my_topic_users/search?q=test5
    @action(detail=False, methods=['GET'])

    # 종목 코드만 추천
    def search(self, request):
        stock_codes = Recommend_Stock()
        # q = request.query_params.get('q', None) 
        print(stock_codes)
        qs = self.get_queryset().filter(stock_code=stock_codes[0])
        serializer = self.get_serializer(qs, many=True)
        
        return Response(serializer.data)

    # 해당 종목 조회하는 함수
    def search_by_detail(self, request):
        
        pass

    # 외국인 비중이 높은 종목 TOP 5
    

class StockTableViewSet(viewsets.ModelViewSet):
    queryset = StockTable.objects.all()
    serializer_class = StockTableSerializer

    permission_classes = [permissions.IsAuthenticated]