from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),                 # This handles the root URL
    path('index.html', views.index, name='index'),      # Optional, if you're directly navigating to index.html
    path('AdminLogin.html', views.AdminLogin, name='AdminLogin'),
    path('AdminLoginAction', views.AdminLoginAction, name='AdminLoginAction'),
    path('TrainCNN', views.TrainCNN, name='TrainCNN'),
    path('DetectActivity.html', views.DetectActivity, name='DetectActivity'),
    path('DetectActivityAction', views.DetectActivityAction, name='DetectActivityAction'),
]
