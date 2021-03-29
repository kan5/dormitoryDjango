from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='researcher_mp'),
    path('csv/in', views.csv_in, name='csv_in'),
    path('csv/out', views.csv_out, name='csv_out'),
    path('csv/st', views.csv_st, name='csv_st'),
    path('csv/rooms', views.csv_rooms, name='csv_rooms'),
]
