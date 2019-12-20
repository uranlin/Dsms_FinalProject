from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('register/',views.register,name='register'),
    path('Changeinfo/',views.Changeinfo,name='Changeinfo'),
    path('activity/',views.activity,name='activity'),
    path('activity/show/<name>/',views.activityShow,name="activityShow"),
    path('activity/edit/',views.activityEdit,name="activityEdit"),
    path('activity/delete/<name>/',views.activityDelete,name="activityDelete"),
    path('addactivity/',views.AddActivity,name="AddActivity"),
    path('CAL/',views.CAL,name="Club_Attend_List")

]