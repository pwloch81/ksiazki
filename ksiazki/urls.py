from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('lista', views.ksiazkiList, name="lista"),
    path('szczegolowo/<str:pk>/', views.ksiazkiszczegolowo, name="szczegolowo"),

]
