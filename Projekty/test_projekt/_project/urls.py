"""
URL configuration for _project project.

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
from myapp import views

# 127.0.0.1:8000/
# 127.0.0.1:8000/admin/

urlpatterns = [
    path('', views.index_page),
    # path('time/', ), # zde přidejte time_page

    # http://127.0.0.1:8000/url-paths/
    path('url-paths/', views.url_paths),

    path('my-path/', views.my_math),

    path('test-template/', views.test_template),

    path('calculator/', views.calculator),
    
    path('time/', views.time_page),

    path("age/", views.age_page),

    path('admin/', admin.site.urls),

    
]
