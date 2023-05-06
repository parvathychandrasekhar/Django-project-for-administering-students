from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('list/', views.student_list, name='student_list'),
    path('delete/', views.delete_confirm, name='delete_confirm'),

]