"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('book/new', views.new_book, name='new-book'),
    path('book/<int:pk>/edit/', views.edit_book, name ='edit-book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete-book'),
    path('admin/', admin.site.urls),
]
