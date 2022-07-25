"""posts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.decorators import login_required
# from posts.views import BlogHome, BlogPostCreate
import posts.views as pv


app_name = 'posts'


urlpatterns = [
    path('', pv.BlogHome.as_view(), name='home'),
    # path('create/', login_required(pv.BlogPostCreate.as_view()), name='create'),
    path('create/', pv.BlogPostCreate.as_view(), name='create'),
    path('edit/<str:slug>', pv.BlogPostUpdate.as_view(), name='edit'),
    path('delete/<str:slug>', pv.BlogpostDelete.as_view(), name='delete'),
    path('<str:slug>/', pv.BlogPostDetail.as_view(), name='detail'),
]
