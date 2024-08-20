from django.urls import path
from . import views
urlpatterns = [
    path('',views.prediction),
    path('result',views.result, name='result'),
    
]
