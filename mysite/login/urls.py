from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('results/', views.results, name='results'),
    path('regist/', views.regist, name='regist'),
]
