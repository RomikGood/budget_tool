from django.test import TestCase
from ..budgets.factories import UserFactory, BudgetFactory, TranactionFactory


class TestBudgetModels(TestCase):
    def setUp(self):
        self.budget = BudgetFactory(
            name='test name',
            description='test desc'
        )

    def test_default_budget_attrs(self):
        self.assertEqual(self.budget.name, 'test name')
        self.assertEqual(self.budget.description, 'test desc')


class TestTransactionModels(TestCase):
    pass
