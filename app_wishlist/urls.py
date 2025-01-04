from django.urls import path

from .views import wishlist_view, wishlist_add_json, wishlist_del_json, wishlist_json

#  TODO Импортируйте ваше представление

app_name = 'wishlist'

urlpatterns = [
    path('wishlist/', wishlist_view, name='wishlist_view'), # TODO Зарегистрируйте обработчик
    #path('wishlist/', wishlist_json),
    path('wishlist/add/<str:id_product>', wishlist_add_json),
    path('wishlist/del/<str:id_product>', wishlist_del_json),
]