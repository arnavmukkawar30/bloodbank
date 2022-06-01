from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name="home"),
    path("patient",views.patient,name="patient"),
    path("donor",views.donor,name="donor"),
    path("prequested",views.prequested,name="prequested"),
    path("ddonated",views.ddonated,name="ddonated"),
    path("login",views.loginpage,name="login"),
    path("logout",views.logoutUser,name="logout"),
    path("register",views.registerpage,name="register"),
]
