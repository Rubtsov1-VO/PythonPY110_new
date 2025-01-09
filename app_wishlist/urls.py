from django.urls import path

from .views import wishlist_view, wishlist_add_json, wishlist_del_json, wishlist_json, wishlist_buy_now_view, \
    wishlist_remove_view

#  TODO Импортируйте ваше представление

app_name = 'wishlist'

urlpatterns = [
    path('wishlist/', wishlist_view, name='wishlist_view'), # TODO Зарегистрируйте обработчик
    #path('wishlist/', wishlist_json),
    path('wishlist/add/<str:id_product>', wishlist_add_json),
    path('wishlist/del/<str:id_product>', wishlist_del_json),
    path('wishlist/buy/<str:id_product>', wishlist_buy_now_view, name="add_now"),
    path('wishlist/remove/<str:id_product>', wishlist_remove_view, name="del_now"),
    path('wishlist/<str:id_product>', wishlist_json)
]