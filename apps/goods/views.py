from django.shortcuts import render

# Create your views here.
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import goods
class GoodsListView(APIView):
    def get(self, request, format=None):
        good_list = goods.objects.all()
        goods_serializer = GoodsSerializer(good_list, many=True, context={"request": request})
        data = {
            "code": 20000,
            "data": goods_serializer.data
        }
        return Response(data)