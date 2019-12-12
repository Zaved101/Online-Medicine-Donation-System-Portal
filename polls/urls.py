from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('index/',views.index, name='index'),
    path('StorePatientInformation/',views.store, name = 'StorePatientInformation'),
    path('StorePatientInformationView/',views.viewstore, name = 'StorePatientInformationView'),
    path('StorePatientInformationEdit/<int:pk>',views.updateStore, name = 'StorePatientInformationEdit'),
    path('StorePatientInformationDelete/<int:pk>',views.deleteStore, name = 'StorePatientInformationDelete'),
    path('done/<int:pk>',views.givemedicine, name = 'done'),
    path('showrx/',views.showrx, name='showrx'),
    path('store/',views.store_Medi, name='store'),
    path('provide/',views.provide_Medi, name='provide'),
    path('medi/', views.givemediview, name='medi'),
    path('adminlogout/',views.user_logout, name='adminlogout'),
]