from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/<str:title>', views.tasks),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name= '/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= '/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('calendar/', views.schedulemeetings)
]