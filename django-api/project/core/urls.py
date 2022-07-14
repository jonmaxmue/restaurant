# chat/urls.py
from django.urls import path
from .views.UserViewSet import UserViewSet

app_name = "core"

urlpatterns = [
    # App paths
    path('core/csrf/', UserViewSet.as_view({'get': 'get_csrf_token'}), name='get_csrf'),
    path('core/log_in/', UserViewSet.as_view({'post': 'login'}), name='user_login'), # the router should be create users/send-mail-token and here the paths are not neccessary but there where a 405?
    path('core/log_out/', UserViewSet.as_view({'get': 'log_out'}), name='user_logout'), # the router should be create users/send-mail-token and here the paths are not neccessary but there where a 405?
    path('core/user-send-sms-code/', UserViewSet.as_view({'post': 'send_sms_code'}), name='user_send_sms_code'), # the router should be create users/send-mail-token and here the paths are not neccessary but there where a 405?
    path('core/user-send-mail-token/', UserViewSet.as_view({'post': 'send_mail_token'}), name='user_send_mail_token'), # the router should be create users/send-mail-token and here the paths are not neccessary but there where a 405?


    path('users/<id>/update-phone-number/', UserViewSet.as_view({'post': 'update_phone_number'}),
         name='user_update_phone_number'), # the router should be create users/send-mail-token and here the paths are not neccessary but there where a 405?
    path('users/<id>/update-email/', UserViewSet.as_view({'post': 'update_email'}),
         name='user_update_email'), # the router should be create users/send-mail-token and here the paths are not neccessary but there where a 405?
    #path('profiles/<id>/', views.ProfileViewSet.as_view({'patch': 'partial_update'}), name='profile_partial_update'),
]
