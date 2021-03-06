import factory
from django.contrib.auth.models import User
from board.models import Transaction, Budget


class UserFactory(factory.django.DjangoModelFactory):
    """Create a test user for writing tests."""

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BudgetFactory(factory.django.DjangoModelFactory):
    """Create a test budget for writing tests."""

    class Meta:
        model = Budget

    user = factory.SubFactory(UserFactory)
    name = 'name'
    total_budget = 55.5


class TransactionFactory(factory.django.DjangoModelFactory):
    """Create a test transaction for writing tests."""

    class Meta:
        model = Transaction

    assigned_to = factory.SubFactory(UserFactory)
    budget = factory.SubFactory(BudgetFactory)
    amount = 55.5
    description = factory.Faker('paragraph')
