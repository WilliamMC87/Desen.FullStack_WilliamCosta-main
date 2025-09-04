from rest_framework import serializers
from .models import CustomUser, Token, Account, AccountToken, Transaction, Bet


# ---------- SERIALIZER DO USUÁRIO ----------
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'name', 'email', 'cpf', 'rg', 'birth_date',
            'address_street', 'address_number', 'address_district',
            'address_zip_code', 'address_city', 'address_state', 'address_country',
            'phone', 'photo', 'creation_date'
        ]
        read_only_fields = ['id', 'creation_date']


# ---------- SERIALIZER DO TOKEN ----------
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['id', 'name', 'code', 'description', 'token_creation_date', 'insertion_date', 'conversion_rate']
        read_only_fields = ['id', 'token_creation_date', 'insertion_date']


# ---------- SERIALIZER DA CONTA ----------
class AccountSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)  # Mostra informações do usuário
    user_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='user', write_only=True)

    class Meta:
        model = Account
        fields = ['id', 'user', 'user_id', 'opening_date', 'closing_date', 'conversion_rate']
        read_only_fields = ['id', 'opening_date']


# ---------- SERIALIZER ACCOUNT TOKEN ----------
class AccountTokenSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    account_id = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), source='account', write_only=True)
    token = TokenSerializer(read_only=True)
    token_id = serializers.PrimaryKeyRelatedField(queryset=Token.objects.all(), source='token', write_only=True)

    class Meta:
        model = AccountToken
        fields = ['id', 'account', 'account_id', 'token', 'token_id', 'balance']
        read_only_fields = ['id']


# ---------- SERIALIZER TRANSACTION ----------
class TransactionSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    account_id = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), source='account', write_only=True)
    token_source = TokenSerializer(read_only=True)
    token_source_id = serializers.PrimaryKeyRelatedField(queryset=Token.objects.all(), source='token_source', write_only=True, allow_null=True)
    token_target = TokenSerializer(read_only=True)
    token_target_id = serializers.PrimaryKeyRelatedField(queryset=Token.objects.all(), source='token_target', write_only=True, allow_null=True)

    class Meta:
        model = Transaction
        fields = [
            'id', 'account', 'account_id', 'transaction_date',
            'token_source', 'token_source_id',
            'token_target', 'token_target_id',
            'token_source_amount', 'token_target_amount',
            'input_amount', 'output_amount',
            'value1', 'value2', 'value3',
            'bet_date'
        ]
        read_only_fields = ['id', 'transaction_date', 'bet_date']


# ---------- SERIALIZER BET ----------
class BetSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    account_id = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), source='account', write_only=True)

    class Meta:
        model = Bet
        fields = ['id', 'account', 'account_id', 'is_loss', 'created_at']
        read_only_fields = ['id', 'created_at']
