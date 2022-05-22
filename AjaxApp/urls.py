from django.urls import path
from .views import CrudHome, Home

app_name = 'AjaxApp'

urlpatterns = [
    path('', CrudHome.as_view(), name= 'Home'),
    #path('create/', CrudCreate.as_view(), name='crud_create' ),
    path('crud/', Home)
]
