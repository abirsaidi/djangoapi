
from django.urls import path,include
from .views import  MarkCreateView ,MarkUpdateView,MarkListView,MarkDetailView,MarkDeleteView
urlpatterns = [
        path('marque-Create/', MarkCreateView.as_view(), name='create-marque'),
        path('marque-Update/<int:pk>/', MarkUpdateView.as_view(), name='update-marque'),
        path ('marque-List/', MarkListView.as_view(), name='list-marque'),
        path('marque-Delete/<int:pk>/', MarkDeleteView.as_view(), name='delete-marque'),
        path('marque-Details/<int:pk>/', MarkDetailView.as_view(), name='details-marque'),

]
