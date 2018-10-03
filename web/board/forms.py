from django.forms import ModelForm
from .models import Transaction, Budget


class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'total_budget']