from django.urls import path
from .views import *


urlpatterns = [
    path("list/", blog_list, name= 'blog-list'),
    path("<int:pk>/detail/", blog_detail, name= "blog-detail")
]