from django.urls import path
from . import views

urlpatterns = [
    path('',views.notes, name='notes'),
    path('items/', views.fridgeitems, name='fridgeitems')
]
