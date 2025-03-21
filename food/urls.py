from django.urls import path

from . import views

app_name = "food"
urlpatterns = [
    path('', views.IndexClassView.as_view(), name="index"),
    path('item/', views.item, name="item"),
    path('<int:pk>/', views.FoodDetailView.as_view(), name="detail"),
    path("add", views.CreateItem.as_view(), name ="add"),
    path("update/<int:item_id>", views.update_item, name ="update"),
    path("delete/<int:item_id>", views.delete_item, name ="delete"),
]