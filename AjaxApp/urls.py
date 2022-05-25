from django.urls import path
from .views import Home, DeleteInfo

app_name = 'AjaxApp'

urlpatterns = [
    #path('', CrudHome.as_view(), name= 'Home'),
    #path('create/', CrudCreate.as_view(), name='crud_create' ),
    path('', Home, name='home'),
    path('delete/<pk>/', DeleteInfo.as_view(), name= 'delete'),
]
