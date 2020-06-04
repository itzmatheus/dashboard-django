from django.urls import path, include

from .views import index, getDataChart

urlpatterns = [
    path('', index, name='home-index'),
    path('data/chart', getDataChart, name='home-data-chart'),
]
