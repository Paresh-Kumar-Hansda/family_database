from django.urls import path
from . import views



urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.PersonListView.as_view(), name='person'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
