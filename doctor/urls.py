from django.urls import path
from . import views
urlpatterns = [
  path('login/', views.user_login, name='user_login'),
  path('show/',views.show, name='show'),
  path('give/',views.give_pre, name='give'),
  # path('rxlist/<int:Patient_ID>',views.rxlist, name='rxlist'),
  path('StorePatientInformationEdit/<int:pk>',views.updateStore, name = 'StorePatientInformationEdit'),
  path('profileview/',views.profile,name='profileview'),
  path('update/',views.upprofile,name='update'),

  path('logout/',views.user_logout, name='logout'),

]