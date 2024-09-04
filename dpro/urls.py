"""
URL configuration for dpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from dpro import views
from dpro import program

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard),
    path('calculator/',views.calculator),
    path('card/', views.card),
    path('time_table/', views.time_table),
    path('armstrong/', views.armstrong),
    path('contact/<int:id>', views.contact),
    path('about/<id>/<name>', views.about),
    path('findevenodd/', views.findevenodd),
    path('series/', program.seriesForm),
]
