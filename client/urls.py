
from django.urls import path,include
from .views import ClientCreateView , ClientListView ,ClientDetailView  ,ClientUpdateView 
urlpatterns = [
      path('client-create/', ClientCreateView.as_view(), name='create-client'),
   path('client-liste/', ClientListView.as_view(), name='liste-client'),
   path('client-detail/<int:pk>/', ClientDetailView.as_view(), name='detail-client'),
   path('client-update/<int:pk>/', ClientUpdateView.as_view(), name='update-client'),
]
