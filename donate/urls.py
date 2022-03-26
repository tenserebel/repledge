from django.urls import path

from . import views

urlpatterns = [
    path('donate/', views.index, name='index'),
    path('donate/<int:pk>/',views.details, name="details")
]