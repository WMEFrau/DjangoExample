from django.urls import path
from . import views

urlpatterns = [
    path('listado', views.listado , name="listado"),
    path('app/create_post', views.create_post , name="create_post"),
    path('app/view_post', views.view_post , name="view_post"),
    path('app/delete_post/<int:id>/', views.delete_post , name="delete_post"),

]
