from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from core.views.ContactViewSet import ContactViewSet
from reservation.views.RestaurantViewSet import RestaurantViewSet
from reservation.views.TableViewSet import TableViewSet
from reservation.views.SeatViewSet import SeatViewSet
from core.views.UserViewSet import UserViewSet

user_router = routers.DefaultRouter()
user_router.register(r'api/users', UserViewSet, basename="user")
restaurant_router = routers.DefaultRouter()
restaurant_router.register(r'api/restaurants', RestaurantViewSet, basename='restaurant')
table_router = routers.DefaultRouter()
table_router.register(r'api/tables', TableViewSet, basename='table')
seat_router = routers.DefaultRouter()
seat_router.register(r'api/seats', SeatViewSet, basename='seat')

urlpatterns = [
    # NOT NESTED
    path('admin/', admin.site.urls),
    path('api/', include(user_router.urls)),
]

urlpatterns += user_router.urls
urlpatterns += restaurant_router.urls
urlpatterns += table_router.urls
urlpatterns += seat_router.urls

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)