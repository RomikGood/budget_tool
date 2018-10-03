from django.urls import path
from .views import BudgetListView, TransactionDetailView, BudgetCreateView

urlpatterns = [
    path('budget', BudgetListView.as_view(), name='budget_view'),
    path('budget/new', BudgetCreateView.as_view(), name='budget_create_view'),
    path('transaction/<int:id>', TransactionDetailView.as_view(), name='transaction_detail'),
]
