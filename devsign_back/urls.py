"""
URL configuration for devsign_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from devsign_app.views import CompanyAPIViewDetails, UserAPIViewController
from devsign_app.views.company import CompanyAPIView
from devsign_app.views.document import DocumentAPIViewController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', CompanyAPIView.as_view()),
    path('company/<company_id>/', CompanyAPIViewDetails.as_view()),
    path('document/', DocumentAPIViewController.as_view()),
    path('user/', UserAPIViewController.as_view()),
]
