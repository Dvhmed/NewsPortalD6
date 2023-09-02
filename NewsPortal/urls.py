"""NewsPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from newsapp import views
from newsapp.views import upgrade_user, CategoryListView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('search/', include('newsapp.urls'), name='post_search'),
    path('news/create/', views.NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit', views.NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete', views.NewsDelete.as_view(), name='news_delete'),
    path('article/create/', views.ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit', views.ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete', views.ArticleDelete.as_view(), name='article_delete'),
    path("accounts/", include("allauth.urls")),
    path('upgrade/', upgrade_user, name='account_upgrade'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
]
