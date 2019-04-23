import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator

User = get_user_model()
from rest_framework.response import Response
#验证字段
class UserRegSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(required=True,allow_blank=False,label="用户名",
                                      validators=[UniqueValidator(queryset=User.objects.all(),message="用户已存在")])

    password = serializers.CharField(style={'input_type': 'password'},label="密码")
    class Meta:
        model = User
        fields = ("user_name","user_phone","password")
        extra_kwargs = {'password': {'write_only': True}}#为了防止密码明文传过来被截获

    #如果不用signals修改成密文也可以用这样方法实现
    def create(self, validated_data):
        user = super(UserRegSerializer,self).create(validated_data = validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate(self, attrs):
        attrs["user_phone"] = attrs["user_name"]
        return attrs


from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    #role = RoleSerializer()#假如想看User的role的信息既可以这样写
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列表类
    """

    class Meta:
        model = User
        fields = ("username", "user_avator","is_superuser")
