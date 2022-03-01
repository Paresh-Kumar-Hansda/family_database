from django.urls import path
from . import views



urlpatterns = [
    #path('', views.index, name='index'),
    path('persons', views.PersonListView.as_view(), name='persons'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('identy/', views.identy, name='identy'),
    path('jharsewa/', views.jharsewa, name='jharsewa'),
    path('education/', views.edu, name='education'),
    path('', views.index, name='index'),
    path('person/<int:pk>/update', views.idupdate, name='idupdate'),
    path('person/<int:pk>/delete', views.id_del, name='id_del'),

]
