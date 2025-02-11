
from django.urls import path,include
from .views import   CategoryCreateview , CategoryListView, CategoryDetailView,CategoryUpdateview, CategoryDeleteView
urlpatterns = [
         path('categorie-Create/', CategoryCreateview.as_view(), name='create-categorie'),
        path('categorie-Update/<int:pk>/', CategoryUpdateview.as_view(), name='update-categorie'),
        path ('categorie-List/', CategoryListView.as_view(), name='list-categorie'),
        path('categorie-Delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete-categorie'),
        path('categorie-Details/<int:pk>/', CategoryDetailView.as_view(), name='details-categorie'),

]