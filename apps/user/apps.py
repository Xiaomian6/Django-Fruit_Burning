from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'


    # #当运行post后运行signals,将密码设置为密文
    # def ready(self):
    #     import user.signals
