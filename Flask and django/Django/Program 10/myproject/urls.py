from django.contrib import admin
from django.urls import path
from pages.views import (
    StudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentListView.as_view(), name='student_list'),
    path('add/', StudentCreateView.as_view(), name='student_add'),
    path('edit/<int:pk>/', StudentUpdateView.as_view(), name='student_edit'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
]
