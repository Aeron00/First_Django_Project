from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('register/',views.register, name='register'),
    path('done', views.done, name='regsuccess'),
    path('login_page',views.login_page, name='login'),
    path('loginsave',views.loginsave, name='logsuccess'),
    path('show',views.show, name='show'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),  
    path('delete/<int:id>/', views.delete),
    path('deletedata/<int:id>', views.deletedata),
    path('search', views.search),
]
