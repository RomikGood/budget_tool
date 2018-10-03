from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db import models


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=180, default='Untitled')
    total_budget = models.FloatField()
    remaining_budget = models.FloatField()
    # date_uploaded = models.DateField(auto_now_add=True)
    # date_modified = models.DateField(auto_now=True)

    def __repr__(self):
        return '<Budget: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Transaction(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction', null=True, blank=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transaction')
    
    amount = models.FloatField()
     
    description = models.TextField(blank=True, null=True)

    # date_uploaded = models.DateField(auto_now_add=True)
    # date_modified = models.DateField(auto_now=True)
    # date_completed = models.DateField(blank=True, null=True)


    # STATES = (
    #     ('WITHDRAWAL', 'Withdrawal'),
    #     ('DEPOSIT', 'Deposit'),
    # )
    # type = models.CharField(
    #     max_length=16,
    #     types=STATES,
    #     # default='None'
    # )

    def __repr__(self):
        return '<Transaction: {} | {}>'.format(self.amount, self.amount)

    # def __str__(self):
    #     return '{} | {}'.format(self.amount, self.amount)



