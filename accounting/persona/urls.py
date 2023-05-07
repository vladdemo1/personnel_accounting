from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('unit-list/', views.unit_list, name='unit-list'),
    path('unit-detail/<str:pk>/', views.unit_detail, name='unit-detail'),
    path('unit-create/', views.unit_create, name="unit-create"),
    path('unit-update/<str:pk>/', views.unit_update, name="unit-update"),
    path('unit-delete/<str:pk>/', views.unit_delete, name="unit-delete"),
    path('attendance-list/', views.attendance_list, name="attendance-list"),
    path('attendance-create/<str:pk>/', views.attendance_create, name="attendance-create"),
    path('unit-premium/<str:pk>/', views.unit_premium, name="unit-premium"),
]
