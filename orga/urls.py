#from turtle import home
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .import views
from django.conf.urls.static import static
from orgaworks.settings import STATIC_URL,STATIC_ROOT
#from django.conf.urls import url
from django.conf import settings
urlpatterns = [
    path('', views.home,name='home'),
    path('home', views.home,name='home'),
    path('vegetables', views.vegetables,name='vegetables'),
    path('exotic', views.exotic,name='exotic'),
    path('fruits', views.fruits,name='fruits'),
    path('<int:id>/productdescription', views.productdescription,name='productdescription'),
    path(r'^$', views.searchitems, name='searchitems'),
    path('about', views.about, name='about'),
    path('internships',views.internships,name="internships"),
    
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('<int:id>/Blogdescription', views.Blogdescription,name='Blogdescription'),
    
]
if settings.DEBUG:
    urlpatterns  +=  static(STATIC_URL, document_root=STATIC_ROOT)
