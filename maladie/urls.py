from django.urls import path,include
from .views import MaladieCreateView, MaladieDetailView, MaladieUpdateView, MaladieDeleteView, MaladieListView 
urlpatterns = [
      path('maladie/', MaladieCreateView.as_view(), name='maladie-create'),
      path('maladie/<int:pk>/', MaladieDetailView.as_view(), name='maladie-detail'),
      path('maladie/<int:pk>/update/', MaladieUpdateView.as_view(), name='maladie-update'),
      path('maladie/<int:pk>/delete/', MaladieDeleteView.as_view(), name='maladie-delete'),
      path('maladie/list/', MaladieListView.as_view(), name='maladie-list'),

]