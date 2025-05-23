from django.urls import path
from . import views
from .views import ProtectedView

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
