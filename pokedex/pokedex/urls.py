from django.urls import include, path
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('pokedex_app.urls')),
    path('', include('pokemon.urls')),
]


