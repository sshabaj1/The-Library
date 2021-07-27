from django.urls import path
from . import views
from .views import HomeView, PostDetailsView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [

    # path('', views.home, name = 'home' ),
    path('', HomeView.as_view(), name = 'home'),
    path('post-details/<int:pk>', PostDetailsView.as_view(), name = 'post-details'),
    path('add_post/',AddPostView.as_view(), name = 'add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name = 'delete_post'),
    path('add_category/',AddCategoryView.as_view(), name = 'add_category'),
    path('category/<str:cats>/', CategoryView, name = 'category')



]
