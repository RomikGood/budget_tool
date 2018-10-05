from django.contrib.auth.models import User
from board.models import Budget, Transaction
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Budget
        fields = ('id', 'name', 'total_amount', 'remaining_budget')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    budget = serializers.HyperlinkedRelatedField(view_name='budget-api', read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'assigned_to', 'budget', 'amount', 'description')