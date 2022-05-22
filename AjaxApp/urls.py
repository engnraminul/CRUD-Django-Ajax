from django.urls import path
from .views import Home

app_name = 'AjaxApp'

urlpatterns = [
    path('', Home, name= 'Home')
]
