from django.contrib import admin
from django.urls import path
from .views import index, sobre, projetos, contato    


app_name = 'page'


urlpatterns = [
    path('home', index, name='home'),
    path('sobre', sobre, name='sobre'),
    path('projetos', projetos, name='projetos'),
    path('contato', contato, name='contato'),
]
