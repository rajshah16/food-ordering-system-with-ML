from . import views
from django.urls import path

urlpatterns = [
    path('' , views.menu , name='MainCourse'),
    path('beverages' , views.beverage , name='Beverage'),
    path('breakfast' , views.breakfast , name='Breakfast'),
    path('chapatis' , views.chapatis , name='Chapatis'),
    path('soup' , views.soup , name='Soup'),
    path('dessert' , views.dessert , name='Dessert'),
    path('cart' , views.cart , name='Cart'),
    path('checkout' , views.checkout , name='Checkout'),
    path('update_item' , views.updateItem , name = 'UpdateItem'),
    path('update_itembf' , views.updateItembf , name="UpdateItembf"),
    path('update_itembev' , views.updateItembev , name = "UpdateItembev"),
    path('update_itemchp' , views.updateItemchp , name="UpdateItemchp"),
    path('update_itemsoup' , views.updateItemsoup , name="UpdateItemsoup"),
    path('update_itemdessert' , views.updateItemdessert , name="UpdateItemdessert")


]
