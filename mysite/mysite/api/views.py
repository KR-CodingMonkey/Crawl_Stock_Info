
## window
# from rest_framework import viewsets
# from rest_framework import permissions
# from mysite.api.models import My6StockTable, StockTable
# from mysite.api.serializers import My6StockTableSerializer, StockTableSerializer
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from mysite.recommend_stock import Recommend_Stock

# class My6TopicTableViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = My6StockTable.objects.all()
#     serializer_class = My6StockTableSerializer

#     permission_classes = [permissions.IsAuthenticated]

#     # /my_topic_users/search?q=test5
#     @action(detail=False, methods=['GET'])

#     # 종목 코드만 추천
#     def search(self, request):
#         stock_codes = Recommend_Stock()
#         # q = request.query_params.get('q', None) 
#         print(stock_codes)
#         qs = self.get_queryset().filter(stock_code=stock_codes[0])
#         serializer = self.get_serializer(qs, many=True)
        
#         return Response(serializer.data)

#     # 외국인 비중이 높은 종목 TOP 5
    

# class StockTableViewSet(viewsets.ModelViewSet):
#     queryset = StockTable.objects.all()
#     serializer_class = StockTableSerializer

#     permission_classes = [permissions.IsAuthenticated]

## Linux
from rest_framework import viewsets
from rest_framework import permissions
from mysite.api.models import My6StockTable, StockTable
from mysite.api.serializers import My6StockTableSerializer, StockTableSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from mysite.recommend_stock import Recommend_Stock
from mysite.stock_graph import My_Graph
from django.shortcuts import render
import base64

class My6TopicTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = My6StockTable.objects.all()
    serializer_class = My6StockTableSerializer

    permission_classes = [permissions.IsAuthenticated]

    # /my_topic_users/search?q=test5
    @action(detail=False, methods=['GET'])
    # 종목 코드만 추천
    def recommend_stock(self, request):
        stock_codes = Recommend_Stock()
        stock_data=[]
        # q = request.query_params.get('q', None) 
        print(stock_codes)
        for code in stock_codes:
            qs = self.get_queryset().filter(stock_code=code)
            serializer = self.get_serializer(qs, many=True)
            stock_data.append((serializer.data)[-1])

        return Response(stock_data)

    # 해당 code 그래프가 저장된 이미지 파일 경로 표현
    @action(detail=False, methods=['GET'])
    def info_detail(self, request):
        q = request.query_params.get('q', None) # user input
        with open(My_Graph(str(q)), "rb") as image_file: # 함수 
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        ctx = {'image': image_data}

        # render (request, index경로, ctx) fix-it
        return render(request, 'C:\\Users\\A0501660\\Work\\project\\mysite\\mysite\\index.html', ctx)

    # 외국인 비중이 높은 종목 TOP 5
    def trading_rank(self, request):
        
        stock_data=[]
        print(stock_codes)

        for code in stock_codes:
            qs = self.get_queryset().filter(stock_code=code)
            serializer = self.get_serializer(qs, many=True)
            stock_data.append((serializer.data)[-1])

        return Response(stock_data)
class StockTableViewSet(viewsets.ModelViewSet):
    queryset = StockTable.objects.all()
    serializer_class = StockTableSerializer

    permission_classes = [permissions.IsAuthenticated]