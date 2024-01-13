from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
path('',views.index,name="index"),
path('product_list/',views.Product_List_View,name="product-list"),
path('product/<pid>/',views.ProductDetail,name='product-detail'),
path('category_list/',views.Category_List_View,name="category-list"),
path('category_list/<cid>/',views.Product_Category_List,name="product-category-list"),
path('tag/<slug:slug_tag>/',views.product_tag,name='tag'),
path('review/<int:pid>/',views.review,name='review'),
path('search/',views.search,name='search'),
path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]
