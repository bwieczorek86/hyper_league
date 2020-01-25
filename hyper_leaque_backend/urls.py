from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='teams_list'),
    path('details/<int:team_id>', views.team_details, name='team_details')
]
