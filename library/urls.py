"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
import rest_framework
from catalog import views
from catalog import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', viewsets.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^catalog[\/]?$', views.catalog_list),

    path('books', views.BookCreate.as_view()),
    path('book/<pk>/', views.BookUpdate.as_view()),
    path('authors', views.AuthorCreate.as_view()),
    path('authors/list', views.AuthorList.as_view()),
    
    path('', include(router.urls)),
    path('api', include('rest_framework.urls', namespace = 'rest_framework')),

    path('catalog/books', views.new_book),
    path('catalog/book/<pk>/update', views.update_book),
    
    # /catalog/planeta/books?year=2020
    # re_path(r'catalog\/(?p<editorial>[a-zA-Z]+)\/books',views.get_books_by_editorial) 
    path('catalog/<editorial>/books', views.get_books_by_editorial)
]
