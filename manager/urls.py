from django.urls import path
from . import views


urlpatterns = [
    path('editor', views.editor, name='mg_editor'),
    path('form/<int:pk>', views.StudentView.as_view(), name='mg_form'),
    path('new_student', views.new_student, name='mg_new_student'),
    path('student_delete/<int:pk>', views.StudentDelete.as_view(), name='mg_student_delete'),
    path('rooms', views.rooms, name='mg_rooms'),
    path('room_form/<int:pk>', views.RoomsView.as_view(), name='mg_room_form'),
    path('room_add', views.RoomsCreate.as_view(), name='mg_room_add'),
    path('room_delete/<int:pk>', views.RoomsDelete.as_view(), name='mg_room_delete'),
]
