from django.urls import path
from . import views 
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
        path('',views.home, name='home' ),
        # Eldho Mathew
        path('newlyassignleads',views.newlyassignleads, name='newlyassignleads' ),
        # Sambhu v pillai
        path('currentleads',views.currentleads, name='currentleads' ),
        path('previousleads',views.previousleads, name='previousleads' ),

]