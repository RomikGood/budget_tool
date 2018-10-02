from django.urls import path
from .views import CategoryListView, CardDetailView

urlpatterns = [
    path('category', CategoryListView.as_view(), name='category_view'),
    path('card/<int:id>', CardDetailView.as_view(), name='card_detail'),
]
