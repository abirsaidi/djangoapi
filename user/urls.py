
from django.urls import path,include
from .views import UserCreateView , UserListView ,UserDetailView  ,UserUpdateView, UserRegisterView   

urlpatterns = [
   path('user-create/', UserCreateView.as_view(), name='create-user'),
   path('user-liste/', UserListView.as_view(), name='liste-user'),
   path('user-detail/<int:pk>/', UserDetailView.as_view(), name='detail-user'),
   path('user-update/<int:pk>/', UserUpdateView.as_view(), name='update-user'),
   path('user-register/', UserRegisterView.as_view(), name='register-user'),
]

