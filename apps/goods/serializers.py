from .models import goods
from rest_framework import serializers

class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = goods
        fields = '__all__'