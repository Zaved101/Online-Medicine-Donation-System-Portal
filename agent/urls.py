from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index, name='index'),
    path('patientAgent/', views.storeAgent, name='patientAgent'),
    path('storemedi/', views.medistore, name='storemedi'),
]