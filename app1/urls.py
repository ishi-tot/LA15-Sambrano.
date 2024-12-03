from django.urls import path
from . import views
app_name = 'app1'

# URL Cofiguration
urlpatterns = [
    path('hello/', views.say_hello),
    path('hi/', views.say_hi),
    path('posts/', views.blog_list),
    path('posts/<int:id>/', views.blog_detail, name='blog_detail'),
]