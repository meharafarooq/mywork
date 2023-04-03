from django.urls import path
from.import views
app_name='appcoffee'
urlpatterns=[
    path('',views.index,name='index'),
    ]