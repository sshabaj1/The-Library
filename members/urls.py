from django.urls import path
from .views import UserRegisterView, UserEditView


urlpatterns = [

    # path('', views.home, name = 'home' ),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),


]
