from django.urls import path
from . import views
# from users import views as user_views
urlpatterns = [
    path('donner_medi/', views.give_medi, name='donner_medi'),
    # path('donner_regi/', views.register, name='donner_regi'),
]