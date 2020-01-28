from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from beers import views

urlpatterns = [
    path('beers/', views.BeerList.as_view()),
    path('beers/<int:pk>/', views.BeerDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)