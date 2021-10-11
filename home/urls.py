from django.urls import path
from  . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:id>',views.portfolio_details,name="details"),

]